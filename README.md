# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--15_01:27:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **206,463 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-15 01:27:15 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:20:36 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:19:33 | Baddegama (Gin Ganga) | 0.84 | 🟢 Normal | -0.034 |  |
| 2026-07-15 01:13:33 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:10:59 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:09:52 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-07-15 01:06:36 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-07-15 01:06:34 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:05:32 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.021 |  |
| 2026-07-15 01:04:27 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:04:07 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.021 |  |
| 2026-07-15 01:03:58 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | -0.010 |  |
| 2026-07-15 01:03:57 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:03:57 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-07-15 01:03:55 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:03:41 | Siyambalanduwa (Heda Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:03:35 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:02:55 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.013 |  |
| 2026-07-15 01:02:44 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:02:42 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:02:21 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-15 01:02:09 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-07-15 01:02:08 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:01:57 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-15 01:01:56 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-15 01:01:47 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | -0.020 |  |
| 2026-07-15 01:01:23 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:01:19 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-07-15 01:01:03 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:00:40 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:00:19 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.099 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-14 22:01:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-07-15 01:00:19 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-07-15 01:01:19 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-07-14 18:02:37 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-07-15 01:09:52 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-07-15 00:38:05 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-15 01:01:56 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-15 01:06:36 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-07-15 01:02:21 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-15 01:01:57 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-15 01:01:23 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:00:40 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:02:44 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:02:42 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:01:03 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-14 18:03:13 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:03:55 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:27:15 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:13:33 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:03:35 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:20:36 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:03:41 | Siyambalanduwa (Heda Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-15 00:04:59 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:03:57 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:04:27 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-07-14 18:01:22 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 00:02:51 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:06:34 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:10:59 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:02:08 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 01:03:58 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | -0.010 |  |
| 2026-07-15 01:02:09 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-07-15 01:02:55 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.013 |  |
| 2026-07-15 01:03:57 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-07-15 01:01:47 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | -0.020 |  |
| 2026-07-15 01:04:07 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.021 |  |
| 2026-07-15 01:05:32 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.021 |  |
| 2026-07-15 01:19:33 | Baddegama (Gin Ganga) | 0.84 | 🟢 Normal | -0.034 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)