# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--16_17:38:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **47,326 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 17:38:45 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | -0.024 |  |
| 2026-01-16 17:14:15 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:13:56 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:13:39 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.064 |  |
| 2026-01-16 17:13:10 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:12:12 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:11:40 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:10:46 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | -0.011 |  |
| 2026-01-16 17:10:31 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:08:14 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:07:23 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-16 17:07:04 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:06:32 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | -0.022 |  |
| 2026-01-16 17:04:13 | Dunamale (Aththanagalu Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-01-16 17:04:08 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-16 17:03:55 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-16 17:03:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.85 | 🟢 Normal | -0.039 |  |
| 2026-01-16 17:03:29 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:03:18 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 17:03:01 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-16 17:03:00 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-16 17:02:53 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-01-16 17:02:48 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 17:02:47 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-01-16 17:02:34 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:02:21 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:02:17 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.020 |  |
| 2026-01-16 17:02:11 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:02:05 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | -0.023 |  |
| 2026-01-16 17:01:59 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:01:56 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:01:42 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-01-16 17:01:36 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-16 17:01:17 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.129 |  |
| 2026-01-16 17:01:15 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:01:11 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:00:44 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | -0.071 |  |
| 2026-01-16 17:00:35 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:00:31 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 17:03:01 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-16 17:04:08 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-16 17:03:18 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 17:02:48 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 17:13:10 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:01:15 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:03:29 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:00:35 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:02:11 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:02:21 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:00:31 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:13:56 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:07:04 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:12:12 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:08:14 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:01:56 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:11:40 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:10:31 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:01:11 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:14:15 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:01:59 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-16 17:07:23 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-16 17:04:13 | Dunamale (Aththanagalu Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-01-16 17:03:00 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-16 17:03:55 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-16 17:01:36 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-16 16:01:53 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-01-16 17:01:42 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-01-16 17:10:46 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | -0.011 |  |
| 2026-01-16 17:02:53 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-01-16 17:02:17 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.020 |  |
| 2026-01-16 17:06:32 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | -0.022 |  |
| 2026-01-16 17:02:05 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | -0.023 |  |
| 2026-01-16 17:38:45 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | -0.024 |  |
| 2026-01-16 17:02:47 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-01-16 17:03:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.85 | 🟢 Normal | -0.039 |  |
| 2026-01-16 17:13:39 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.064 |  |
| 2026-01-16 17:00:44 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | -0.071 |  |
| 2026-01-16 17:01:17 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.129 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)