# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--15_19:34:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **73,976 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 19:34:27 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.048 |  |
| 2026-02-15 19:18:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.078 |  |
| 2026-02-15 19:14:35 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.041 |  |
| 2026-02-15 19:08:22 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.079 |  |
| 2026-02-15 19:08:17 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-02-15 19:06:56 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:06:42 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:06:41 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:06:41 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.018 |  |
| 2026-02-15 19:06:27 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:06:24 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:06:13 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:04:51 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:04:06 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:04:03 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-15 19:03:56 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.029 |  |
| 2026-02-15 19:03:44 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | -0.010 |  |
| 2026-02-15 19:03:35 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:03:35 | Glencourse (Kelani Ganga) | 8.26 | 🟢 Normal | -0.021 |  |
| 2026-02-15 19:03:18 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.011 |  |
| 2026-02-15 19:03:16 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.608 | 🔺 Rising |
| 2026-02-15 19:02:46 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:02:21 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:02:10 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:01:49 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-02-15 19:01:45 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:01:41 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-02-15 19:01:35 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:01:12 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:01:08 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-02-15 19:00:42 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.050 |  |
| 2026-02-15 19:00:25 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 18:59:54 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-02-15 18:58:23 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 19:03:16 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.608 | 🔺 Rising |
| 2026-02-15 19:04:03 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-15 19:00:25 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 19:02:21 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:01:45 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:03:35 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:01:12 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:02:48 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:01:35 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:02:10 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:06:27 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:04:51 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:06:41 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:04:06 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:02:46 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:06:24 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:06:42 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:01:14 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:06:56 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:58:23 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:06:13 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-15 19:01:49 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-02-15 19:08:17 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-02-15 19:03:44 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | -0.010 |  |
| 2026-02-15 18:59:54 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-02-15 19:03:18 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.011 |  |
| 2026-02-15 19:06:41 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.018 |  |
| 2026-02-15 19:01:08 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-02-15 18:04:25 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-02-15 19:01:41 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-02-15 19:03:35 | Glencourse (Kelani Ganga) | 8.26 | 🟢 Normal | -0.021 |  |
| 2026-02-15 19:03:56 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.029 |  |
| 2026-02-15 19:14:35 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.041 |  |
| 2026-02-15 19:34:27 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.048 |  |
| 2026-02-15 19:00:42 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.050 |  |
| 2026-02-15 18:00:16 | Weraganthota (Mahaweli Ganga) | -2.47 | 🟢 Normal | -0.064 |  |
| 2026-02-15 19:18:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.078 |  |
| 2026-02-15 19:08:22 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)