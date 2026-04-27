# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--27_16:22:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **136,574 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 16:22:30 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | 0.000 |  |
| 2026-04-27 16:17:52 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-27 16:14:48 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-27 16:14:35 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-27 16:13:07 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.087 |  |
| 2026-04-27 16:12:15 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.011 |  |
| 2026-04-27 16:12:13 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | -0.017 |  |
| 2026-04-27 16:11:57 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | -0.053 |  |
| 2026-04-27 16:09:05 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 16:08:22 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-27 16:08:13 | Dunamale (Aththanagalu Oya) | 0.83 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-04-27 16:06:25 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.119 |  |
| 2026-04-27 16:06:24 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-27 16:06:11 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.057 |  |
| 2026-04-27 16:05:59 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-27 16:05:57 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | -0.058 |  |
| 2026-04-27 16:05:41 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | -0.029 |  |
| 2026-04-27 16:05:23 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-27 16:04:27 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 16:04:24 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2026-04-27 16:04:17 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-27 16:03:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | -0.039 |  |
| 2026-04-27 16:03:29 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.019 |  |
| 2026-04-27 16:03:27 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | -0.028 |  |
| 2026-04-27 16:03:16 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.040 |  |
| 2026-04-27 16:02:26 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-27 16:02:22 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-27 16:02:19 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 16:02:19 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 16:02:18 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-04-27 16:02:08 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-27 16:01:59 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-27 16:01:51 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-27 16:01:50 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-04-27 16:01:49 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-27 16:01:09 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-27 16:00:34 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.011 |  |
| 2026-04-27 16:00:33 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-27 16:00:25 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 16:08:13 | Dunamale (Aththanagalu Oya) | 0.83 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-04-27 16:02:22 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-27 16:05:23 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-27 16:04:17 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-27 16:14:48 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-27 16:14:35 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-27 16:04:27 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 16:09:05 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 16:02:18 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-04-27 16:05:59 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-27 16:02:19 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 16:01:51 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-27 16:02:19 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 16:06:24 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-27 16:00:25 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-27 16:22:30 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | 0.000 |  |
| 2026-04-27 16:17:52 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-27 16:00:33 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-27 16:01:49 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-27 16:04:24 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2026-04-27 16:08:22 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-27 16:01:59 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-27 16:01:09 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-27 16:02:26 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-27 16:02:08 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-27 16:12:15 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.011 |  |
| 2026-04-27 16:00:34 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.011 |  |
| 2026-04-27 16:12:13 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | -0.017 |  |
| 2026-04-27 16:03:29 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.019 |  |
| 2026-04-27 16:01:50 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-04-27 16:03:27 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | -0.028 |  |
| 2026-04-27 16:05:41 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | -0.029 |  |
| 2026-04-27 16:03:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | -0.039 |  |
| 2026-04-27 16:03:16 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.040 |  |
| 2026-04-27 16:11:57 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | -0.053 |  |
| 2026-04-27 16:06:11 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.057 |  |
| 2026-04-27 16:05:57 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | -0.058 |  |
| 2026-04-27 16:13:07 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.087 |  |
| 2026-04-27 16:06:25 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)