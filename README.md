# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_06:33:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **150,431 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 06:33:18 | Galgamuwa (Mee Oya) | 2.10 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-13 06:18:24 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-05-13 06:16:51 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-13 06:13:03 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-05-13 06:11:40 | Rathnapura (Kalu Ganga) | 4.45 | 🟢 Normal | 0.324 | 🔺 Rising |
| 2026-05-13 06:10:09 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-13 06:09:40 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | -0.029 |  |
| 2026-05-13 06:09:38 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.044 |  |
| 2026-05-13 06:09:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.54 | 🟢 Normal | -0.196 |  |
| 2026-05-13 06:09:18 | Dunamale (Aththanagalu Oya) | 2.78 | 🟢 Normal | -0.060 |  |
| 2026-05-13 06:08:29 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-13 06:07:22 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | 0.000 |  |
| 2026-05-13 06:07:01 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 06:07:00 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | -0.153 |  |
| 2026-05-13 06:06:54 | Katharagama (Menik Ganga) | 0.85 | 🟢 Normal | -0.061 |  |
| 2026-05-13 06:05:57 | Glencourse (Kelani Ganga) | 10.29 | 🟢 Normal | -0.077 |  |
| 2026-05-13 06:05:51 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-05-13 06:05:39 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | -0.012 |  |
| 2026-05-13 06:05:21 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-13 06:04:59 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.108 |  |
| 2026-05-13 06:04:22 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-13 06:04:21 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-05-13 06:04:20 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-13 06:04:19 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-13 06:03:55 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.094 |  |
| 2026-05-13 06:03:51 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | -0.021 |  |
| 2026-05-13 06:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-05-13 06:02:42 | Putupaula (Kalu Ganga) | 1.12 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-05-13 06:02:41 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-05-13 06:02:24 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-13 06:02:18 | Thanamalwila (Kirindi Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-13 06:02:17 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.062 |  |
| 2026-05-13 06:02:11 | Panadugama (Nilwala Ganga) | 3.49 | 🟢 Normal | -0.024 |  |
| 2026-05-13 06:01:43 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 06:01:30 | Weraganthota (Mahaweli Ganga) | -2.63 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-13 06:01:22 | Moragaswewa (Deduru Oya) | 1.82 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-05-13 06:01:20 | Moraketiya (Walawe Ganga) | 1.61 | 🟢 Normal | 0.559 | 🔺 Rising |
| 2026-05-13 06:01:20 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.021 |  |
| 2026-05-13 06:01:13 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-05-13 06:01:07 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-13 06:00:32 | Nakkala (Kumbukkan Oya) | 1.46 | 🟢 Normal | -0.045 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 06:02:42 | Putupaula (Kalu Ganga) | 1.12 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-05-13 06:01:20 | Moraketiya (Walawe Ganga) | 1.61 | 🟢 Normal | 0.559 | 🔺 Rising |
| 2026-05-13 06:11:40 | Rathnapura (Kalu Ganga) | 4.45 | 🟢 Normal | 0.324 | 🔺 Rising |
| 2026-05-13 06:01:22 | Moragaswewa (Deduru Oya) | 1.82 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-05-13 06:04:21 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-05-13 06:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-05-13 06:01:13 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-05-13 06:13:03 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-05-13 06:05:51 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-05-13 06:01:07 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-13 06:05:21 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-13 06:33:18 | Galgamuwa (Mee Oya) | 2.10 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-13 06:01:30 | Weraganthota (Mahaweli Ganga) | -2.63 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-13 06:10:09 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-13 06:02:24 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-13 06:07:01 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 06:08:29 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-13 06:01:43 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 06:18:24 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-05-13 06:04:22 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-13 06:07:22 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | 0.000 |  |
| 2026-05-13 06:16:51 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-13 06:02:18 | Thanamalwila (Kirindi Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-13 06:05:39 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | -0.012 |  |
| 2026-05-12 18:01:07 | Thanthirimale (Malwathu Oya) | 3.38 | 🟢 Normal | -0.020 |  |
| 2026-05-13 06:03:51 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | -0.021 |  |
| 2026-05-13 06:01:20 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.021 |  |
| 2026-05-13 06:02:11 | Panadugama (Nilwala Ganga) | 3.49 | 🟢 Normal | -0.024 |  |
| 2026-05-13 06:09:40 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | -0.029 |  |
| 2026-05-13 06:09:38 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.044 |  |
| 2026-05-13 06:00:32 | Nakkala (Kumbukkan Oya) | 1.46 | 🟢 Normal | -0.045 |  |
| 2026-05-13 06:09:18 | Dunamale (Aththanagalu Oya) | 2.78 | 🟢 Normal | -0.060 |  |
| 2026-05-13 06:06:54 | Katharagama (Menik Ganga) | 0.85 | 🟢 Normal | -0.061 |  |
| 2026-05-13 06:02:17 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.062 |  |
| 2026-05-13 06:05:57 | Glencourse (Kelani Ganga) | 10.29 | 🟢 Normal | -0.077 |  |
| 2026-05-13 06:03:55 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.094 |  |
| 2026-05-13 06:04:59 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.108 |  |
| 2026-05-13 06:07:00 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | -0.153 |  |
| 2026-05-13 06:09:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.54 | 🟢 Normal | -0.196 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)