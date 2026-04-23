# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--23_23:40:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **133,272 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 23:40:16 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.004 |  |
| 2026-04-23 23:33:01 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-23 23:32:03 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-23 23:25:01 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | -54.000 |  |
| 2026-04-23 23:24:59 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -54.000 |  |
| 2026-04-23 23:17:58 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-23 23:13:23 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.028 |  |
| 2026-04-23 23:11:25 | Thanamalwila (Kirindi Oya) | 2.41 | 🟢 Normal | -0.080 |  |
| 2026-04-23 23:10:27 | Panadugama (Nilwala Ganga) | 3.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-23 23:10:26 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-23 23:10:22 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.094 |  |
| 2026-04-23 23:10:18 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-23 23:09:04 | Hanwella (Kelani Ganga) | 1.35 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-04-23 23:08:44 | Peradeniya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-23 23:07:13 | Katharagama (Menik Ganga) | 0.49 | 🟢 Normal | 0.616 | 🔺 Rising |
| 2026-04-23 23:05:25 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-04-23 23:04:45 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.011 |  |
| 2026-04-23 23:04:12 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-23 23:03:55 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 23:07:13 | Katharagama (Menik Ganga) | 0.49 | 🟢 Normal | 0.616 | 🔺 Rising |
| 2026-04-23 23:02:31 | Dunamale (Aththanagalu Oya) | 1.54 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2026-04-23 21:01:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-04-23 23:09:04 | Hanwella (Kelani Ganga) | 1.35 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-04-23 23:01:10 | Ellagawa (Kalu Ganga) | 5.38 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-04-23 23:03:14 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-23 22:06:14 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-23 23:08:44 | Peradeniya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-23 23:10:26 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-23 23:02:18 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-23 23:10:27 | Panadugama (Nilwala Ganga) | 3.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-23 23:02:47 | Glencourse (Kelani Ganga) | 9.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-23 23:00:14 | Manampitiya (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-23 23:04:12 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-23 23:10:18 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-23 23:03:55 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 18:03:04 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 23:40:16 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.004 |  |
| 2026-04-23 18:01:09 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-04-23 23:33:01 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-23 23:17:58 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-23 23:00:32 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-23 23:01:18 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-23 23:05:25 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-04-23 23:02:38 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-04-23 18:03:04 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-04-23 23:03:11 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | -0.010 |  |
| 2026-04-23 23:04:45 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.011 |  |
| 2026-04-23 23:01:18 | Kuda Oya (Kirindi Oya) | 2.45 | 🟢 Normal | -0.020 |  |
| 2026-04-23 23:02:27 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-04-23 23:02:15 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | -0.021 |  |
| 2026-04-23 23:13:23 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.028 |  |
| 2026-04-23 23:02:34 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.028 |  |
| 2026-04-23 23:02:38 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-04-23 23:02:53 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.041 |  |
| 2026-04-23 23:11:25 | Thanamalwila (Kirindi Oya) | 2.41 | 🟢 Normal | -0.080 |  |
| 2026-04-23 23:10:22 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.094 |  |
| 2026-04-23 23:00:34 | Moraketiya (Walawe Ganga) | 1.49 | 🟢 Normal | -1.707 |  |
| 2026-04-23 23:25:01 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | -54.000 |  |

## River Water Level Charts by Station

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)