# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_16:12:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **147,221 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 16:12:49 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.037 |  |
| 2026-05-09 16:09:55 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | -0.025 |  |
| 2026-05-09 16:09:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.45 | 🟢 Normal | -0.089 |  |
| 2026-05-09 16:08:42 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | -0.039 |  |
| 2026-05-09 16:08:03 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-05-09 16:07:55 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-09 16:07:47 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-05-09 16:07:04 | Putupaula (Kalu Ganga) | 1.23 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-09 16:07:01 | Thanthirimale (Malwathu Oya) | 3.33 | 🟢 Normal | -0.029 |  |
| 2026-05-09 16:06:05 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-09 16:06:02 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | -0.049 |  |
| 2026-05-09 16:05:36 | Katharagama (Menik Ganga) | 1.97 | 🟢 Normal | -0.131 |  |
| 2026-05-09 16:05:13 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-05-09 16:05:09 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-05-09 16:05:00 | Thanamalwila (Kirindi Oya) | 2.32 | 🟢 Normal | -0.077 |  |
| 2026-05-09 16:04:37 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.133 |  |
| 2026-05-09 16:04:29 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-09 16:04:17 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-09 16:04:06 | Hanwella (Kelani Ganga) | 1.36 | 🟢 Normal | -0.049 |  |
| 2026-05-09 16:03:35 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.011 |  |
| 2026-05-09 16:03:29 | Galgamuwa (Mee Oya) | 2.39 | 🟢 Normal | -0.063 |  |
| 2026-05-09 16:03:24 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | -0.030 |  |
| 2026-05-09 16:03:13 | Glencourse (Kelani Ganga) | 9.43 | 🟢 Normal | -0.032 |  |
| 2026-05-09 16:03:03 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 16:02:52 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-09 16:02:13 | Moragaswewa (Deduru Oya) | 3.60 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-05-09 16:02:09 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-05-09 16:02:02 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-09 16:01:38 | Kuda Oya (Kirindi Oya) | 2.36 | 🟢 Normal | -0.049 |  |
| 2026-05-09 16:01:16 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-09 16:01:10 | Ellagawa (Kalu Ganga) | 6.30 | 🟢 Normal | -0.050 |  |
| 2026-05-09 16:01:00 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-05-09 16:00:53 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-09 16:00:53 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-05-09 16:00:20 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-09 16:00:17 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | -0.010 |  |
| 2026-05-09 16:00:17 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-09 16:00:13 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | -0.005 |  |
| 2026-05-09 15:59:42 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 16:02:13 | Moragaswewa (Deduru Oya) | 3.60 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-05-09 16:02:52 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-09 16:01:16 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-09 16:06:05 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-09 16:07:55 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-09 16:07:04 | Putupaula (Kalu Ganga) | 1.23 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-09 16:00:20 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-09 16:00:17 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-09 16:03:03 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 16:04:17 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-09 15:05:24 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-09 16:04:29 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-09 16:02:02 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-09 16:00:53 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-09 16:00:13 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | -0.005 |  |
| 2026-05-09 16:05:13 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-05-09 16:00:17 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | -0.010 |  |
| 2026-05-09 16:08:03 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-05-09 16:02:09 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-05-09 16:05:09 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-05-09 16:00:53 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-05-09 16:07:47 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-05-09 16:03:35 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.011 |  |
| 2026-05-09 16:01:00 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-05-09 16:09:55 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | -0.025 |  |
| 2026-05-09 16:07:01 | Thanthirimale (Malwathu Oya) | 3.33 | 🟢 Normal | -0.029 |  |
| 2026-05-09 16:03:24 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | -0.030 |  |
| 2026-05-09 16:03:13 | Glencourse (Kelani Ganga) | 9.43 | 🟢 Normal | -0.032 |  |
| 2026-05-09 16:12:49 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.037 |  |
| 2026-05-09 16:08:42 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | -0.039 |  |
| 2026-05-09 16:01:38 | Kuda Oya (Kirindi Oya) | 2.36 | 🟢 Normal | -0.049 |  |
| 2026-05-09 16:04:06 | Hanwella (Kelani Ganga) | 1.36 | 🟢 Normal | -0.049 |  |
| 2026-05-09 16:06:02 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | -0.049 |  |
| 2026-05-09 16:01:10 | Ellagawa (Kalu Ganga) | 6.30 | 🟢 Normal | -0.050 |  |
| 2026-05-09 16:03:29 | Galgamuwa (Mee Oya) | 2.39 | 🟢 Normal | -0.063 |  |
| 2026-05-09 16:05:00 | Thanamalwila (Kirindi Oya) | 2.32 | 🟢 Normal | -0.077 |  |
| 2026-05-09 16:09:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.45 | 🟢 Normal | -0.089 |  |
| 2026-05-09 16:05:36 | Katharagama (Menik Ganga) | 1.97 | 🟢 Normal | -0.131 |  |
| 2026-05-09 16:04:37 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.133 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)