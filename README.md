# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--24_05:15:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **160,233 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-24 05:15:23 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-24 05:14:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.66 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-24 05:13:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.66 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-24 05:12:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.67 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-24 05:10:41 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-05-24 05:09:49 | Rathnapura (Kalu Ganga) | 4.76 | 🟢 Normal | -0.072 |  |
| 2026-05-24 05:08:14 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | -0.022 |  |
| 2026-05-24 05:07:06 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-24 05:07:05 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-24 05:06:47 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-24 05:05:43 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.013 |  |
| 2026-05-24 05:05:30 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-05-24 05:05:13 | Ellagawa (Kalu Ganga) | 10.14 | 🟡 Alert | 0.000 |  |
| 2026-05-24 05:05:02 | Deraniyagala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.011 |  |
| 2026-05-24 05:04:43 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-05-24 05:04:07 | Putupaula (Kalu Ganga) | 3.30 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-24 05:03:58 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | -0.074 |  |
| 2026-05-24 05:03:37 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-24 05:02:48 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-24 05:02:22 | Hanwella (Kelani Ganga) | 5.06 | 🟢 Normal | -0.050 |  |
| 2026-05-24 05:02:18 | Dunamale (Aththanagalu Oya) | 4.11 | 🟡 Alert | -0.091 |  |
| 2026-05-24 05:02:16 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | -0.011 |  |
| 2026-05-24 05:02:12 | Glencourse (Kelani Ganga) | 11.07 | 🟢 Normal | -0.062 |  |
| 2026-05-24 05:02:11 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-24 05:01:58 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-24 05:01:56 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | -0.014 |  |
| 2026-05-24 05:01:53 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.090 |  |
| 2026-05-24 05:01:52 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-05-24 05:01:43 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-24 05:01:32 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-24 05:01:31 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-24 05:01:21 | Magura (Kalu Ganga) | 2.57 | 🟢 Normal | -0.030 |  |
| 2026-05-24 05:01:06 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-24 05:01:00 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-24 05:00:49 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-24 05:14:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.66 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-24 05:04:07 | Putupaula (Kalu Ganga) | 3.30 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-24 05:05:13 | Ellagawa (Kalu Ganga) | 10.14 | 🟡 Alert | 0.000 |  |
| 2026-05-24 05:02:18 | Dunamale (Aththanagalu Oya) | 4.11 | 🟡 Alert | -0.091 |  |
| 2026-05-24 05:01:58 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-24 05:15:23 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-24 05:01:00 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 18:00:13 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-24 05:01:31 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-24 04:01:26 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-24 05:01:43 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-24 05:02:48 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:04:23 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-24 05:00:49 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-24 05:01:32 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-24 04:08:25 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-24 05:01:06 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-24 05:03:37 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-24 05:07:06 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-24 05:06:47 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-24 00:22:42 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-24 05:02:11 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-24 05:10:41 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-05-24 05:04:43 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-05-24 04:04:28 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-05-23 18:01:26 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-05-24 05:05:30 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-05-24 05:01:52 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-05-24 05:02:16 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | -0.011 |  |
| 2026-05-24 05:05:02 | Deraniyagala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.011 |  |
| 2026-05-24 05:05:43 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.013 |  |
| 2026-05-24 05:01:56 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | -0.014 |  |
| 2026-05-24 05:08:14 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | -0.022 |  |
| 2026-05-24 05:01:21 | Magura (Kalu Ganga) | 2.57 | 🟢 Normal | -0.030 |  |
| 2026-05-24 05:02:22 | Hanwella (Kelani Ganga) | 5.06 | 🟢 Normal | -0.050 |  |
| 2026-05-24 05:02:12 | Glencourse (Kelani Ganga) | 11.07 | 🟢 Normal | -0.062 |  |
| 2026-05-24 05:09:49 | Rathnapura (Kalu Ganga) | 4.76 | 🟢 Normal | -0.072 |  |
| 2026-05-24 05:03:58 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | -0.074 |  |
| 2026-05-24 05:01:53 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)