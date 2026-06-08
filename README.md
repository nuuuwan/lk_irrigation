# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--08_23:09:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **174,189 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 23:09:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.54 | 🟢 Normal | -0.117 |  |
| 2026-06-08 23:08:25 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | -0.023 |  |
| 2026-06-08 23:08:15 | Rathnapura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.029 |  |
| 2026-06-08 23:07:22 | Baddegama (Gin Ganga) | 2.51 | 🟢 Normal | -0.020 |  |
| 2026-06-08 23:07:08 | Glencourse (Kelani Ganga) | 11.72 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-08 23:06:35 | Deraniyagala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.103 |  |
| 2026-06-08 23:06:17 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.061 |  |
| 2026-06-08 23:06:16 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 23:05:35 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.010 |  |
| 2026-06-08 23:05:30 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-08 23:05:29 | Dunamale (Aththanagalu Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-06-08 23:04:45 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.021 |  |
| 2026-06-08 23:04:26 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-08 23:04:26 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-08 23:03:59 | Hanwella (Kelani Ganga) | 3.41 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-06-08 23:03:46 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-06-08 23:03:45 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-08 23:03:16 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-08 23:03:00 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.059 |  |
| 2026-06-08 23:02:32 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-06-08 23:02:31 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-08 23:02:28 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-08 23:02:16 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-08 23:02:04 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | -0.011 |  |
| 2026-06-08 23:02:01 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-08 23:01:47 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-08 23:01:27 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-06-08 23:01:15 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-08 23:00:26 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-08 23:00:26 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-06-08 23:00:25 | Nawalapitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -0.064 |  |
| 2026-06-08 22:19:00 | Ellagawa (Kalu Ganga) | 6.72 | 🟢 Normal | 0.000 |  |
| 2026-06-08 22:17:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.64 | 🟢 Normal | -0.117 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 23:01:27 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-06-08 23:03:59 | Hanwella (Kelani Ganga) | 3.41 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-06-08 23:07:08 | Glencourse (Kelani Ganga) | 11.72 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-08 23:02:01 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-08 18:00:59 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-08 22:02:09 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-08 23:03:45 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-08 23:03:16 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-08 23:02:16 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-08 23:01:47 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-08 23:00:26 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-08 18:07:32 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-08 22:15:43 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-08 23:05:30 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-08 22:19:00 | Ellagawa (Kalu Ganga) | 6.72 | 🟢 Normal | 0.000 |  |
| 2026-06-08 23:06:16 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 23:04:26 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-08 22:03:28 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-08 23:05:29 | Dunamale (Aththanagalu Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-06-08 23:02:31 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-08 23:03:46 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-06-08 23:04:26 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-08 23:01:15 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-08 22:08:43 | Putupaula (Kalu Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-06-08 23:02:32 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-06-08 23:05:35 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.010 |  |
| 2026-06-08 23:00:26 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-06-08 23:02:04 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | -0.011 |  |
| 2026-06-08 22:10:53 | Magura (Kalu Ganga) | 2.36 | 🟢 Normal | -0.018 |  |
| 2026-06-08 23:07:22 | Baddegama (Gin Ganga) | 2.51 | 🟢 Normal | -0.020 |  |
| 2026-06-08 23:04:45 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.021 |  |
| 2026-06-08 23:08:25 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | -0.023 |  |
| 2026-06-08 23:08:15 | Rathnapura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.029 |  |
| 2026-06-08 18:02:35 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.040 |  |
| 2026-06-08 23:03:00 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.059 |  |
| 2026-06-08 23:06:17 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.061 |  |
| 2026-06-08 23:00:25 | Nawalapitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -0.064 |  |
| 2026-06-08 23:06:35 | Deraniyagala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.103 |  |
| 2026-06-08 23:09:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.54 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)