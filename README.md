# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--22_13:18:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **158,769 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 13:18:09 | Rathnapura (Kalu Ganga) | 7.84 | 🟠 Minor Flood | -0.024 |  |
| 2026-05-22 13:15:17 | Panadugama (Nilwala Ganga) | 3.13 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-05-22 13:12:39 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-22 13:10:20 | Magura (Kalu Ganga) | 4.37 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-05-22 13:10:18 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.027 |  |
| 2026-05-22 13:09:42 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.038 |  |
| 2026-05-22 13:09:31 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-05-22 13:09:01 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-05-22 13:08:27 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-22 13:07:32 | Badalgama (Maha Oya) | 4.08 | 🟢 Normal | -0.046 |  |
| 2026-05-22 13:07:09 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-22 13:06:45 | Dunamale (Aththanagalu Oya) | 5.00 | 🟠 Minor Flood | 0.063 | 🔺 Rising |
| 2026-05-22 13:06:23 | Glencourse (Kelani Ganga) | 15.46 | 🟡 Alert | 0.059 | 🔺 Rising |
| 2026-05-22 13:05:40 | Nagalagam Street (Kelani Ganga) | 1.16 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-22 13:05:18 | Putupaula (Kalu Ganga) | 2.08 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-05-22 13:04:56 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-05-22 13:04:32 | Holombuwa (Kelani Ganga) | 1.11 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-05-22 13:04:14 | Hanwella (Kelani Ganga) | 8.03 | 🟠 Minor Flood | 0.110 | 🔺 Rising |
| 2026-05-22 13:04:05 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-22 13:03:41 | Deraniyagala (Kelani Ganga) | 2.44 | 🟢 Normal | -0.317 |  |
| 2026-05-22 13:03:31 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-22 13:03:16 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-22 13:03:05 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-22 13:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.41 | 🟡 Alert | 0.121 | 🔺 Rising |
| 2026-05-22 13:02:25 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 13:02:22 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-05-22 13:02:21 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-22 13:02:10 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.020 |  |
| 2026-05-22 13:02:09 | Ellagawa (Kalu Ganga) | 9.07 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-05-22 13:02:08 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-22 13:01:52 | Thawalama (Gin Ganga) | 3.55 | 🟢 Normal | -0.134 |  |
| 2026-05-22 13:01:28 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-22 13:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-22 13:00:57 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.011 |  |
| 2026-05-22 13:00:44 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-22 13:00:33 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.053 |  |
| 2026-05-22 13:00:07 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 13:04:14 | Hanwella (Kelani Ganga) | 8.03 | 🟠 Minor Flood | 0.110 | 🔺 Rising |
| 2026-05-22 13:06:45 | Dunamale (Aththanagalu Oya) | 5.00 | 🟠 Minor Flood | 0.063 | 🔺 Rising |
| 2026-05-22 13:18:09 | Rathnapura (Kalu Ganga) | 7.84 | 🟠 Minor Flood | -0.024 |  |
| 2026-05-22 13:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.41 | 🟡 Alert | 0.121 | 🔺 Rising |
| 2026-05-22 13:06:23 | Glencourse (Kelani Ganga) | 15.46 | 🟡 Alert | 0.059 | 🔺 Rising |
| 2026-05-22 13:10:20 | Magura (Kalu Ganga) | 4.37 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-05-22 13:15:17 | Panadugama (Nilwala Ganga) | 3.13 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-05-22 13:09:01 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-05-22 13:05:18 | Putupaula (Kalu Ganga) | 2.08 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-05-22 13:02:09 | Ellagawa (Kalu Ganga) | 9.07 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-05-22 13:05:40 | Nagalagam Street (Kelani Ganga) | 1.16 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-22 13:04:32 | Holombuwa (Kelani Ganga) | 1.11 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-05-22 13:02:22 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-05-22 13:00:44 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-22 13:07:09 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-22 13:01:28 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-22 13:00:07 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 13:08:27 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-22 13:02:08 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-22 12:00:38 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-22 13:02:25 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 13:04:05 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-22 13:03:05 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-22 13:03:31 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-22 13:12:39 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-22 13:02:21 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-22 13:09:31 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-05-22 13:03:16 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-22 13:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-22 13:04:56 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-05-22 13:00:57 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.011 |  |
| 2026-05-22 12:00:34 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.017 |  |
| 2026-05-22 13:02:10 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.020 |  |
| 2026-05-22 13:10:18 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.027 |  |
| 2026-05-22 13:09:42 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.038 |  |
| 2026-05-22 13:07:32 | Badalgama (Maha Oya) | 4.08 | 🟢 Normal | -0.046 |  |
| 2026-05-22 13:00:33 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.053 |  |
| 2026-05-22 13:01:52 | Thawalama (Gin Ganga) | 3.55 | 🟢 Normal | -0.134 |  |
| 2026-05-22 13:03:41 | Deraniyagala (Kelani Ganga) | 2.44 | 🟢 Normal | -0.317 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)