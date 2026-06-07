# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--07_16:33:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **173,035 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 16:33:58 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | -0.014 |  |
| 2026-06-07 16:31:29 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-07 16:19:34 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-07 16:16:06 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-07 16:13:48 | Panadugama (Nilwala Ganga) | 3.24 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-07 16:07:57 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.019 |  |
| 2026-06-07 16:07:33 | Badalgama (Maha Oya) | 2.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 16:06:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.74 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-07 16:06:40 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.019 |  |
| 2026-06-07 16:06:36 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-06-07 16:05:47 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-07 16:05:45 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-07 16:05:31 | Magura (Kalu Ganga) | 3.65 | 🟢 Normal | -0.041 |  |
| 2026-06-07 16:05:13 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-07 16:05:06 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | -0.029 |  |
| 2026-06-07 16:04:50 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 16:04:49 | Baddegama (Gin Ganga) | 2.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-07 16:04:07 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-06-07 16:03:50 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-07 16:03:47 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-07 16:03:37 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-07 16:03:26 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-07 16:03:15 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 16:03:05 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-07 16:03:05 | Glencourse (Kelani Ganga) | 12.10 | 🟢 Normal | -0.102 |  |
| 2026-06-07 16:02:49 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.098 |  |
| 2026-06-07 16:02:41 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-06-07 16:02:21 | Deraniyagala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-06-07 16:02:19 | Rathnapura (Kalu Ganga) | 4.28 | 🟢 Normal | -0.138 |  |
| 2026-06-07 16:02:11 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-06-07 16:02:10 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-07 16:02:03 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-06-07 16:01:58 | Putupaula (Kalu Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-06-07 16:01:56 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-07 16:01:46 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-06-07 16:01:37 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-07 16:01:06 | Ellagawa (Kalu Ganga) | 7.61 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-07 16:00:49 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 16:00:40 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-07 16:00:29 | Nawalapitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.062 |  |
| 2026-06-07 16:00:18 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 16:02:03 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-06-07 16:01:06 | Ellagawa (Kalu Ganga) | 7.61 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-07 16:03:05 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-07 16:03:47 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-07 16:13:48 | Panadugama (Nilwala Ganga) | 3.24 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-07 16:00:18 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-07 16:04:49 | Baddegama (Gin Ganga) | 2.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-07 16:06:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.74 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-07 16:04:50 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 16:07:33 | Badalgama (Maha Oya) | 2.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 16:03:15 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 16:00:49 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 16:19:34 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-07 16:05:13 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-07 16:01:37 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-07 16:03:37 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-06-07 16:03:26 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-07 16:16:06 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-07 16:01:58 | Putupaula (Kalu Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-06-07 16:00:40 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-07 16:05:47 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-07 16:31:29 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-07 16:03:50 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-07 16:02:10 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-07 16:06:36 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-06-07 16:04:07 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-06-07 16:02:41 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-06-07 16:02:11 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-06-07 16:01:46 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-06-07 16:33:58 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | -0.014 |  |
| 2026-06-07 16:07:57 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.019 |  |
| 2026-06-07 16:06:40 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.019 |  |
| 2026-06-07 16:02:21 | Deraniyagala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-06-07 16:05:06 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | -0.029 |  |
| 2026-06-07 16:05:31 | Magura (Kalu Ganga) | 3.65 | 🟢 Normal | -0.041 |  |
| 2026-06-07 16:00:29 | Nawalapitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.062 |  |
| 2026-06-07 16:02:49 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.098 |  |
| 2026-06-07 16:03:05 | Glencourse (Kelani Ganga) | 12.10 | 🟢 Normal | -0.102 |  |
| 2026-06-07 16:02:19 | Rathnapura (Kalu Ganga) | 4.28 | 🟢 Normal | -0.138 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)