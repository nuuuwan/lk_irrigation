# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--24_14:19:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **188,143 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 14:19:28 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.009 |  |
| 2026-06-24 14:12:07 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-24 14:11:16 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-06-24 14:10:14 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-24 14:10:13 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.041 |  |
| 2026-06-24 14:08:24 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.019 |  |
| 2026-06-24 14:08:17 | Baddegama (Gin Ganga) | 1.74 | 🟢 Normal | -0.020 |  |
| 2026-06-24 14:07:08 | Panadugama (Nilwala Ganga) | 2.83 | 🟢 Normal | -0.019 |  |
| 2026-06-24 14:06:30 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-24 14:06:09 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-24 14:06:03 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.020 |  |
| 2026-06-24 14:05:21 | Putupaula (Kalu Ganga) | 1.95 | 🟢 Normal | -0.088 |  |
| 2026-06-24 14:04:42 | Magura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.021 |  |
| 2026-06-24 14:04:20 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | -0.048 |  |
| 2026-06-24 14:04:07 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-06-24 14:04:04 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-06-24 14:03:35 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-06-24 14:03:17 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | -0.020 |  |
| 2026-06-24 14:03:11 | Glencourse (Kelani Ganga) | 10.61 | 🟢 Normal | 0.000 |  |
| 2026-06-24 14:02:54 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.019 |  |
| 2026-06-24 14:02:50 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-06-24 14:02:46 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-06-24 14:02:33 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-06-24 14:02:32 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-06-24 14:02:27 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-24 14:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.06 | 🟡 Alert | -0.070 |  |
| 2026-06-24 14:02:15 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-24 14:02:11 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 14:02:10 | Dunamale (Aththanagalu Oya) | 2.80 | 🟢 Normal | -0.068 |  |
| 2026-06-24 14:02:07 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-24 14:01:47 | Rathnapura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.034 |  |
| 2026-06-24 14:01:31 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.020 |  |
| 2026-06-24 14:01:25 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-24 14:01:10 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 14:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-24 14:01:07 | Ellagawa (Kalu Ganga) | 6.29 | 🟢 Normal | -0.076 |  |
| 2026-06-24 14:00:09 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 14:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.06 | 🟡 Alert | -0.070 |  |
| 2026-06-24 14:02:07 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-24 13:03:48 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-24 14:02:15 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-24 14:02:27 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-24 14:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-24 13:31:04 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 14:01:10 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 14:11:16 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-06-24 13:06:35 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 14:03:11 | Glencourse (Kelani Ganga) | 10.61 | 🟢 Normal | 0.000 |  |
| 2026-06-24 14:10:14 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-24 14:00:09 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-24 14:06:30 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-24 14:06:09 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-24 14:12:07 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-24 14:02:11 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 14:19:28 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.009 |  |
| 2026-06-24 14:02:32 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-06-24 14:02:33 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-06-24 14:02:46 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-06-24 14:02:50 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-06-24 14:04:04 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-06-24 14:04:07 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-06-24 14:07:08 | Panadugama (Nilwala Ganga) | 2.83 | 🟢 Normal | -0.019 |  |
| 2026-06-24 14:08:24 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.019 |  |
| 2026-06-24 14:02:54 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.019 |  |
| 2026-06-24 14:06:03 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.020 |  |
| 2026-06-24 14:01:31 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.020 |  |
| 2026-06-24 14:08:17 | Baddegama (Gin Ganga) | 1.74 | 🟢 Normal | -0.020 |  |
| 2026-06-24 14:03:17 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | -0.020 |  |
| 2026-06-24 14:03:35 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-06-24 14:04:42 | Magura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.021 |  |
| 2026-06-24 14:01:47 | Rathnapura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.034 |  |
| 2026-06-24 14:10:13 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.041 |  |
| 2026-06-24 14:04:20 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | -0.048 |  |
| 2026-06-24 14:02:10 | Dunamale (Aththanagalu Oya) | 2.80 | 🟢 Normal | -0.068 |  |
| 2026-06-24 14:01:07 | Ellagawa (Kalu Ganga) | 6.29 | 🟢 Normal | -0.076 |  |
| 2026-06-24 14:05:21 | Putupaula (Kalu Ganga) | 1.95 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)