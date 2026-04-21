# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_12:12:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **131,053 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 12:12:39 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.018 |  |
| 2026-04-21 12:12:11 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-21 12:11:53 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-21 12:10:41 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.028 |  |
| 2026-04-21 12:10:29 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-21 12:08:52 | Galgamuwa (Mee Oya) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-04-21 12:08:32 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | -0.098 |  |
| 2026-04-21 12:08:05 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-21 12:07:33 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.021 |  |
| 2026-04-21 12:06:49 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.029 |  |
| 2026-04-21 12:06:23 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-21 12:06:03 | Ellagawa (Kalu Ganga) | 6.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 12:05:35 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-04-21 12:05:06 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.021 |  |
| 2026-04-21 12:05:01 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-21 12:04:43 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-21 12:04:33 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-21 12:04:32 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-04-21 12:04:26 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-21 12:04:20 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-21 12:03:44 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-21 12:03:32 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | -0.058 |  |
| 2026-04-21 12:03:28 | Rathnapura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.152 |  |
| 2026-04-21 12:03:14 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-21 12:03:09 | Hanwella (Kelani Ganga) | 1.85 | 🟢 Normal | -0.060 |  |
| 2026-04-21 12:03:01 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.081 |  |
| 2026-04-21 12:02:52 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.053 |  |
| 2026-04-21 12:02:49 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-04-21 12:02:48 | Thanamalwila (Kirindi Oya) | 1.79 | 🟢 Normal | -0.039 |  |
| 2026-04-21 12:02:46 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-21 12:02:45 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-21 12:02:17 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | -0.031 |  |
| 2026-04-21 12:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 12:01:34 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-21 12:01:19 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-21 12:01:18 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-21 12:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-04-21 12:01:07 | Kuda Oya (Kirindi Oya) | 1.89 | 🟢 Normal | -0.020 |  |
| 2026-04-21 12:01:02 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-21 12:00:41 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-04-21 12:00:11 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.040 |  |
| 2026-04-21 12:00:09 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 12:04:32 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-04-21 12:04:43 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-21 12:00:41 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-04-21 12:04:26 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-21 12:02:45 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-21 12:06:23 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-21 12:01:19 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-21 12:04:20 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-21 12:06:03 | Ellagawa (Kalu Ganga) | 6.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 12:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 12:01:02 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-21 12:01:34 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-21 12:01:18 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-21 12:04:33 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-21 12:12:11 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-21 12:08:05 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-21 12:02:46 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-21 12:03:14 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-21 12:03:44 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-21 12:11:53 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-21 12:08:52 | Galgamuwa (Mee Oya) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-04-21 12:05:35 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-04-21 12:12:39 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.018 |  |
| 2026-04-21 12:01:07 | Kuda Oya (Kirindi Oya) | 1.89 | 🟢 Normal | -0.020 |  |
| 2026-04-21 12:02:49 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-04-21 12:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-04-21 12:07:33 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.021 |  |
| 2026-04-21 12:05:06 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.021 |  |
| 2026-04-21 12:10:41 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.028 |  |
| 2026-04-21 12:06:49 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.029 |  |
| 2026-04-21 12:02:17 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | -0.031 |  |
| 2026-04-21 12:02:48 | Thanamalwila (Kirindi Oya) | 1.79 | 🟢 Normal | -0.039 |  |
| 2026-04-21 12:00:11 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.040 |  |
| 2026-04-21 12:02:52 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.053 |  |
| 2026-04-21 12:03:32 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | -0.058 |  |
| 2026-04-21 12:03:09 | Hanwella (Kelani Ganga) | 1.85 | 🟢 Normal | -0.060 |  |
| 2026-04-21 12:03:01 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.081 |  |
| 2026-04-21 12:08:32 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | -0.098 |  |
| 2026-04-21 12:03:28 | Rathnapura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.152 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)