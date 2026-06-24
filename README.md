# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--25_00:13:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **188,517 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 00:13:49 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-25 00:13:19 | Moragaswewa (Deduru Oya) | 0.12 | 🟢 Normal | 10.232 | 🔺 Rising |
| 2026-06-25 00:13:01 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.009 |  |
| 2026-06-25 00:12:41 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 10.232 | 🔺 Rising |
| 2026-06-25 00:11:38 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 10.232 | 🔺 Rising |
| 2026-06-25 00:09:53 | Hanwella (Kelani Ganga) | 2.27 | 🟢 Normal | -1.481 |  |
| 2026-06-25 00:09:18 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.009 |  |
| 2026-06-25 00:07:58 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.031 |  |
| 2026-06-25 00:07:58 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-06-25 00:07:02 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-06-25 00:06:54 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | -0.010 |  |
| 2026-06-25 00:06:49 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.019 |  |
| 2026-06-25 00:06:09 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | -0.089 |  |
| 2026-06-25 00:06:06 | Putupaula (Kalu Ganga) | 1.46 | 🟢 Normal | -0.044 |  |
| 2026-06-25 00:05:50 | Hanwella (Kelani Ganga) | 2.37 | 🟢 Normal | -1.481 |  |
| 2026-06-25 00:05:29 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | -0.057 |  |
| 2026-06-25 00:05:29 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | -0.018 |  |
| 2026-06-25 00:05:22 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.021 |  |
| 2026-06-25 00:05:10 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-25 00:05:06 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 00:04:46 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-25 00:04:36 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | -0.014 |  |
| 2026-06-25 00:04:30 | Glencourse (Kelani Ganga) | 10.27 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-06-25 00:03:41 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.080 |  |
| 2026-06-25 00:03:38 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-06-25 00:03:08 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-25 00:02:58 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-25 00:02:46 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-25 00:02:46 | Dunamale (Aththanagalu Oya) | 2.03 | 🟢 Normal | -0.039 |  |
| 2026-06-25 00:02:42 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.012 |  |
| 2026-06-25 00:02:40 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-06-25 00:02:32 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-25 00:02:02 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-25 00:01:49 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-25 00:01:43 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-25 00:01:34 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-25 00:01:19 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:33:00 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.018 |  |
| 2026-06-24 23:32:22 | Ellagawa (Kalu Ganga) | 5.75 | 🟢 Normal | -0.089 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-25 00:13:19 | Moragaswewa (Deduru Oya) | 0.12 | 🟢 Normal | 10.232 | 🔺 Rising |
| 2026-06-25 00:04:30 | Glencourse (Kelani Ganga) | 10.27 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-06-25 00:02:46 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-25 00:01:34 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-25 00:02:02 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-25 00:05:06 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-25 00:01:19 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:21 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-25 00:03:08 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-25 00:13:49 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-25 00:01:43 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-25 00:04:46 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-25 00:02:58 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:10 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-24 23:05:31 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-25 00:02:32 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-25 00:05:10 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-25 00:07:02 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-06-25 00:13:01 | Magura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.009 |  |
| 2026-06-25 00:09:18 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.009 |  |
| 2026-06-25 00:06:54 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | -0.010 |  |
| 2026-06-25 00:01:49 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-25 00:02:40 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-06-24 18:00:37 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-06-25 00:03:38 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-06-25 00:02:42 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.012 |  |
| 2026-06-25 00:04:36 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | -0.014 |  |
| 2026-06-25 00:05:29 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | -0.018 |  |
| 2026-06-25 00:06:49 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.019 |  |
| 2026-06-25 00:07:58 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-06-25 00:05:22 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.021 |  |
| 2026-06-24 23:01:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.56 | 🟢 Normal | -0.022 |  |
| 2026-06-25 00:07:58 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.031 |  |
| 2026-06-25 00:02:46 | Dunamale (Aththanagalu Oya) | 2.03 | 🟢 Normal | -0.039 |  |
| 2026-06-25 00:06:06 | Putupaula (Kalu Ganga) | 1.46 | 🟢 Normal | -0.044 |  |
| 2026-06-25 00:05:29 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | -0.057 |  |
| 2026-06-25 00:03:41 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.080 |  |
| 2026-06-25 00:06:09 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | -0.089 |  |
| 2026-06-25 00:09:53 | Hanwella (Kelani Ganga) | 2.27 | 🟢 Normal | -1.481 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)