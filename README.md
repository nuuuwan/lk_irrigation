# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--16_15:13:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **47,245 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 15:13:47 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:11:57 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.029 |  |
| 2026-01-16 15:11:13 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.009 |  |
| 2026-01-16 15:09:00 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:07:44 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:06:43 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.009 |  |
| 2026-01-16 15:05:48 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:04:26 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:04:21 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.029 |  |
| 2026-01-16 15:04:19 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.073 |  |
| 2026-01-16 15:04:17 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-01-16 15:04:13 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:03:55 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.099 |  |
| 2026-01-16 15:03:51 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:03:28 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:03:27 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-01-16 15:03:13 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 15:03:07 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:02:55 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:02:50 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:02:46 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-16 15:02:44 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:02:21 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-01-16 15:02:19 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-01-16 15:02:15 | Thanthirimale (Malwathu Oya) | 1.68 | 🟢 Normal | -0.021 |  |
| 2026-01-16 15:02:10 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | -0.097 |  |
| 2026-01-16 15:02:09 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.93 | 🟢 Normal | -0.030 |  |
| 2026-01-16 15:02:07 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | -0.040 |  |
| 2026-01-16 15:02:07 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:01:55 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:01:51 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:01:27 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-01-16 15:01:26 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:01:13 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-16 15:00:56 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:00:38 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:00:33 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:00:21 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-16 14:46:25 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 15:01:13 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-16 15:02:46 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-16 15:03:13 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 15:00:21 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:02:55 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:00:38 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:01:51 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:03:07 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:03:28 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:02:44 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:07:44 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:01:26 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:03:51 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:01:55 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:04:13 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:09:00 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:00:56 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:02:09 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:05:48 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:13:47 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:02:50 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:02:07 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:04:26 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-16 15:06:43 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.009 |  |
| 2026-01-16 15:11:13 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.009 |  |
| 2026-01-16 14:05:44 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-01-16 15:02:19 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-01-16 15:03:27 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-01-16 15:02:21 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-01-16 15:04:17 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-01-16 15:01:27 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-01-16 15:02:15 | Thanthirimale (Malwathu Oya) | 1.68 | 🟢 Normal | -0.021 |  |
| 2026-01-16 15:04:21 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.029 |  |
| 2026-01-16 15:11:57 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.029 |  |
| 2026-01-16 15:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.93 | 🟢 Normal | -0.030 |  |
| 2026-01-16 15:02:07 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | -0.040 |  |
| 2026-01-16 15:04:19 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.073 |  |
| 2026-01-16 15:02:10 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | -0.097 |  |
| 2026-01-16 15:03:55 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.099 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)