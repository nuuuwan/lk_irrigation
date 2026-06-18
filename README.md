# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--18_14:16:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **182,765 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 14:16:19 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:15:43 | Baddegama (Gin Ganga) | 1.81 | 🟢 Normal | -0.018 |  |
| 2026-06-18 14:15:27 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-06-18 14:10:06 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.058 |  |
| 2026-06-18 14:09:53 | Panadugama (Nilwala Ganga) | 3.55 | 🟢 Normal | -0.039 |  |
| 2026-06-18 14:09:18 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:07:45 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:06:54 | Rathnapura (Kalu Ganga) | 2.11 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-06-18 14:06:38 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:06:29 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:06:29 | Magura (Kalu Ganga) | 2.57 | 🟢 Normal | 0.291 | 🔺 Rising |
| 2026-06-18 14:06:11 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-18 14:05:57 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:05:21 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-18 14:04:56 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.024 |  |
| 2026-06-18 14:04:52 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-18 14:04:51 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:04:10 | Hanwella (Kelani Ganga) | 2.45 | 🟢 Normal | -0.021 |  |
| 2026-06-18 14:03:57 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -90.000 |  |
| 2026-06-18 14:03:55 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:03:55 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -90.000 |  |
| 2026-06-18 14:03:49 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-18 14:03:35 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:03:11 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-06-18 14:03:09 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:02:43 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:02:31 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:02:27 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.064 |  |
| 2026-06-18 14:02:22 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.56 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-06-18 14:02:12 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:01:55 | Ellagawa (Kalu Ganga) | 5.96 | 🟢 Normal | -0.031 |  |
| 2026-06-18 14:01:50 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:01:46 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:01:27 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-06-18 14:01:19 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-06-18 14:01:17 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:00:59 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:00:14 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -2.198 |  |
| 2026-06-18 14:00:11 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 14:06:29 | Magura (Kalu Ganga) | 2.57 | 🟢 Normal | 0.291 | 🔺 Rising |
| 2026-06-18 14:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.56 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-06-18 14:01:27 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-06-18 14:06:54 | Rathnapura (Kalu Ganga) | 2.11 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-06-18 14:03:11 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-06-18 14:15:27 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-06-18 14:05:21 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-18 14:03:49 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-18 14:06:11 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-18 14:04:52 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-18 14:01:50 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-18 13:02:20 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:01:46 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:03:09 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:02:31 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:05:57 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:02:43 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:03:35 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:04:51 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:01:17 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:00:11 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:02:12 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:06:29 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:16:19 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:00:59 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:06:38 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:09:18 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:03:55 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:02:22 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-18 14:01:19 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-06-18 14:15:43 | Baddegama (Gin Ganga) | 1.81 | 🟢 Normal | -0.018 |  |
| 2026-06-18 14:04:10 | Hanwella (Kelani Ganga) | 2.45 | 🟢 Normal | -0.021 |  |
| 2026-06-18 14:04:56 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.024 |  |
| 2026-06-18 14:01:55 | Ellagawa (Kalu Ganga) | 5.96 | 🟢 Normal | -0.031 |  |
| 2026-06-18 14:09:53 | Panadugama (Nilwala Ganga) | 3.55 | 🟢 Normal | -0.039 |  |
| 2026-06-18 14:10:06 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.058 |  |
| 2026-06-18 14:02:27 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.064 |  |
| 2026-06-18 14:00:14 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -2.198 |  |
| 2026-06-18 14:03:57 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -90.000 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)