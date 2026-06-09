# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--09_09:11:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **174,549 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-09 09:11:28 | Rathnapura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.021 |  |
| 2026-06-09 09:08:47 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | -0.019 |  |
| 2026-06-09 09:07:56 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-09 09:06:53 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | -0.049 |  |
| 2026-06-09 09:06:52 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-09 09:06:45 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 09:06:37 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-09 09:06:34 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.021 |  |
| 2026-06-09 09:06:19 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-09 09:06:11 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-09 09:05:51 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | -0.020 |  |
| 2026-06-09 09:05:35 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-09 09:05:09 | Glencourse (Kelani Ganga) | 11.21 | 🟢 Normal | -0.020 |  |
| 2026-06-09 09:04:59 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-06-09 09:04:52 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-06-09 09:04:48 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-09 09:04:22 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-09 09:04:17 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-09 09:04:16 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-06-09 09:03:58 | Putupaula (Kalu Ganga) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-06-09 09:03:42 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-09 09:03:28 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-09 09:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.10 | 🟢 Normal | -0.042 |  |
| 2026-06-09 09:03:22 | Deraniyagala (Kelani Ganga) | 1.37 | 🟢 Normal | -0.052 |  |
| 2026-06-09 09:03:07 | Hanwella (Kelani Ganga) | 3.45 | 🟢 Normal | -0.050 |  |
| 2026-06-09 09:02:54 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-06-09 09:02:46 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 09:02:38 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-09 09:02:21 | Nawalapitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.020 |  |
| 2026-06-09 09:02:12 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 09:02:03 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | -0.050 |  |
| 2026-06-09 09:01:39 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-06-09 09:01:32 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.022 |  |
| 2026-06-09 09:01:32 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-09 09:01:30 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | -0.020 |  |
| 2026-06-09 09:01:23 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.060 |  |
| 2026-06-09 09:01:22 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-09 09:00:53 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 09:00:48 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-09 09:00:42 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-09 09:03:28 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-09 09:05:35 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-09 09:06:19 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-09 09:02:46 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 09:00:53 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 09:06:45 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 09:02:12 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-09 09:04:17 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-09 09:01:32 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-09 09:01:22 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-09 09:04:22 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-09 09:00:48 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-09 09:07:56 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-09 09:03:42 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-09 09:02:38 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-09 09:06:52 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-09 09:04:16 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-06-09 09:04:52 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-06-09 09:06:37 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-09 09:04:59 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-06-09 09:04:48 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-09 09:02:54 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-06-09 09:01:39 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-06-09 09:08:47 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | -0.019 |  |
| 2026-06-09 09:05:09 | Glencourse (Kelani Ganga) | 11.21 | 🟢 Normal | -0.020 |  |
| 2026-06-09 09:02:21 | Nawalapitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.020 |  |
| 2026-06-09 09:03:58 | Putupaula (Kalu Ganga) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-06-09 09:00:42 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-06-09 09:01:30 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | -0.020 |  |
| 2026-06-09 09:05:51 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | -0.020 |  |
| 2026-06-09 09:06:34 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.021 |  |
| 2026-06-09 09:11:28 | Rathnapura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.021 |  |
| 2026-06-09 09:01:32 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.022 |  |
| 2026-06-09 09:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.10 | 🟢 Normal | -0.042 |  |
| 2026-06-09 09:06:53 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | -0.049 |  |
| 2026-06-09 09:03:07 | Hanwella (Kelani Ganga) | 3.45 | 🟢 Normal | -0.050 |  |
| 2026-06-09 09:02:03 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | -0.050 |  |
| 2026-06-09 09:03:22 | Deraniyagala (Kelani Ganga) | 1.37 | 🟢 Normal | -0.052 |  |
| 2026-06-09 09:01:23 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)