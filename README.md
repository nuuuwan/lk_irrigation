# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--24_23:04:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **160,737 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-24 23:04:15 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-05-24 23:04:14 | Ellagawa (Kalu Ganga) | 9.40 | 🟢 Normal | -0.039 |  |
| 2026-05-24 23:04:11 | Deraniyagala (Kelani Ganga) | 2.83 | 🟢 Normal | -0.071 |  |
| 2026-05-24 23:04:02 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-24 23:03:30 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-05-24 23:03:26 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-05-24 23:03:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.12 | 🟡 Alert | -0.022 |  |
| 2026-05-24 23:03:17 | Nawalapitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.117 |  |
| 2026-05-24 23:02:28 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-05-24 23:02:22 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-24 23:02:19 | Dunamale (Aththanagalu Oya) | 2.72 | 🟢 Normal | -0.040 |  |
| 2026-05-24 23:02:16 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-05-24 23:01:56 | Peradeniya (Mahaweli Ganga) | 1.81 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-05-24 23:01:56 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-24 23:01:44 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-24 23:01:42 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-24 23:01:36 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-24 23:01:14 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-24 23:00:54 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-24 23:00:46 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-24 23:00:09 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-24 23:00:07 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-24 22:10:52 | Rathnapura (Kalu Ganga) | 5.23 | 🟡 Alert | 0.161 | 🔺 Rising |
| 2026-05-24 22:04:39 | Putupaula (Kalu Ganga) | 3.26 | 🟡 Alert | -0.010 |  |
| 2026-05-24 23:03:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.12 | 🟡 Alert | -0.022 |  |
| 2026-05-24 22:08:12 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.481 | 🔺 Rising |
| 2026-05-24 23:01:56 | Peradeniya (Mahaweli Ganga) | 1.81 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-05-24 23:02:16 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-05-24 23:00:54 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-24 22:10:31 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-24 23:04:02 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-24 22:06:47 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-24 18:00:57 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-05-24 23:00:09 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-24 23:01:36 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-24 23:02:22 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-24 23:01:56 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-24 22:01:29 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:00:50 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-24 23:03:26 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-05-24 23:01:14 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-24 22:02:07 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-24 22:00:10 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 0.000 |  |
| 2026-05-24 23:00:46 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-24 23:00:07 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-24 22:05:46 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:00:42 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-24 22:05:20 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-24 23:01:42 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-24 23:01:44 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-24 23:03:30 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-05-24 23:02:28 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-05-24 22:03:36 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-05-24 23:04:15 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-05-24 22:03:52 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.019 |  |
| 2026-05-24 22:01:52 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.020 |  |
| 2026-05-24 23:04:14 | Ellagawa (Kalu Ganga) | 9.40 | 🟢 Normal | -0.039 |  |
| 2026-05-24 23:02:19 | Dunamale (Aththanagalu Oya) | 2.72 | 🟢 Normal | -0.040 |  |
| 2026-05-24 23:04:11 | Deraniyagala (Kelani Ganga) | 2.83 | 🟢 Normal | -0.071 |  |
| 2026-05-24 22:06:18 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | -0.079 |  |
| 2026-05-24 23:03:17 | Nawalapitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)