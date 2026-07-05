# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--05_08:22:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **197,756 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 08:22:36 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.022 |  |
| 2026-07-05 08:15:29 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-05 08:13:22 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -18.000 |  |
| 2026-07-05 08:13:20 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | -18.000 |  |
| 2026-07-05 08:13:13 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:10:30 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:09:58 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:09:33 | Nagalagam Street (Kelani Ganga) | 0.44 | 🟢 Normal | -0.015 |  |
| 2026-07-05 08:08:58 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 138.462 | 🔺 Rising |
| 2026-07-05 08:08:46 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:08:45 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:08:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | -0.039 |  |
| 2026-07-05 08:08:32 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 138.462 | 🔺 Rising |
| 2026-07-05 08:08:07 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-07-05 08:07:43 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.057 |  |
| 2026-07-05 08:07:32 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:06:36 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:05:44 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-07-05 08:05:30 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:05:14 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:05:03 | Glencourse (Kelani Ganga) | 11.24 | 🟢 Normal | -0.118 |  |
| 2026-07-05 08:04:38 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.031 |  |
| 2026-07-05 08:04:16 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.029 |  |
| 2026-07-05 08:04:07 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:03:56 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:03:31 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.040 |  |
| 2026-07-05 08:03:29 | Badalgama (Maha Oya) | 3.11 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:03:14 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.042 |  |
| 2026-07-05 08:03:13 | Hanwella (Kelani Ganga) | 3.27 | 🟢 Normal | -0.041 |  |
| 2026-07-05 08:03:12 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:03:03 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:02:10 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:01:51 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:01:44 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:01:41 | Giriulla (Maha Oya) | 1.97 | 🟢 Normal | -0.051 |  |
| 2026-07-05 08:01:22 | Ellagawa (Kalu Ganga) | 5.77 | 🟢 Normal | -0.030 |  |
| 2026-07-05 08:01:16 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | -0.042 |  |
| 2026-07-05 08:01:12 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:01:10 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-05 08:01:10 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.202 |  |
| 2026-07-05 08:00:56 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-05 08:00:13 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 07:46:46 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.057 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 08:08:58 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 138.462 | 🔺 Rising |
| 2026-07-05 08:00:56 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-05 08:01:10 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-05 08:15:29 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-05 08:01:12 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:00:13 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:01:51 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:05:14 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:09:58 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:07:32 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:10:30 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:03:12 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:08:46 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:05:30 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:04:07 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:03:56 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:03:03 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:03:29 | Badalgama (Maha Oya) | 3.11 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:02:10 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:13:13 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:06:36 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:01:44 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-05 08:08:07 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-07-05 08:09:33 | Nagalagam Street (Kelani Ganga) | 0.44 | 🟢 Normal | -0.015 |  |
| 2026-07-05 08:05:44 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-07-05 08:22:36 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.022 |  |
| 2026-07-05 08:04:16 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.029 |  |
| 2026-07-05 08:01:22 | Ellagawa (Kalu Ganga) | 5.77 | 🟢 Normal | -0.030 |  |
| 2026-07-05 08:04:38 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.031 |  |
| 2026-07-05 08:08:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | -0.039 |  |
| 2026-07-05 08:03:31 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.040 |  |
| 2026-07-05 08:03:13 | Hanwella (Kelani Ganga) | 3.27 | 🟢 Normal | -0.041 |  |
| 2026-07-05 08:01:16 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | -0.042 |  |
| 2026-07-05 08:03:14 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.042 |  |
| 2026-07-05 08:01:41 | Giriulla (Maha Oya) | 1.97 | 🟢 Normal | -0.051 |  |
| 2026-07-05 08:07:43 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.057 |  |
| 2026-07-05 08:05:03 | Glencourse (Kelani Ganga) | 11.24 | 🟢 Normal | -0.118 |  |
| 2026-07-05 08:01:10 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.202 |  |
| 2026-07-05 08:13:22 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)