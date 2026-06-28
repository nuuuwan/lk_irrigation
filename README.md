# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--29_05:07:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **192,247 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 05:07:03 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.037 |  |
| 2026-06-29 05:06:54 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-29 05:06:44 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-29 05:06:20 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-06-29 05:05:29 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-29 05:04:53 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.005 |  |
| 2026-06-29 05:04:52 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-29 05:03:57 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-29 05:03:46 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-29 05:03:40 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-29 05:03:32 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-29 05:03:22 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-06-29 05:03:08 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.100 |  |
| 2026-06-29 05:02:52 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-06-29 05:02:31 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-29 05:02:26 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 05:02:17 | Hanwella (Kelani Ganga) | 1.56 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-29 05:02:14 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-29 05:02:06 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.021 |  |
| 2026-06-29 05:02:02 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.118 |  |
| 2026-06-29 05:02:01 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | -0.050 |  |
| 2026-06-29 05:01:48 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 05:01:47 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-29 05:01:33 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-29 05:01:32 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-29 05:01:22 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-29 05:00:53 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:36:56 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-06-29 04:30:35 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:25:36 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-29 04:21:33 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:21:27 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.082 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 03:03:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | 0.621 | 🔺 Rising |
| 2026-06-29 05:06:20 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-06-29 05:03:22 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-06-29 04:09:51 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-06-29 05:01:32 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-29 04:25:36 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-29 05:01:22 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-29 05:02:14 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-29 05:02:17 | Hanwella (Kelani Ganga) | 1.56 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-29 05:06:54 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-29 04:08:06 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-29 04:07:23 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-29 05:01:33 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-29 05:03:46 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-29 05:01:48 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 05:03:40 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-29 05:03:57 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:04:59 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-29 05:04:52 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-29 05:00:53 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-29 05:02:31 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-29 05:03:32 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-29 05:02:26 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 05:01:47 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-29 05:05:29 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:21:33 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-06-29 05:06:44 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:06:41 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-29 04:02:06 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-29 05:04:53 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.005 |  |
| 2026-06-29 05:02:52 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-06-28 18:01:23 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-06-29 05:02:06 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.021 |  |
| 2026-06-29 05:07:03 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.037 |  |
| 2026-06-29 05:02:01 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | -0.050 |  |
| 2026-06-29 04:21:27 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.082 |  |
| 2026-06-29 05:03:08 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.100 |  |
| 2026-06-29 05:02:02 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.118 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)