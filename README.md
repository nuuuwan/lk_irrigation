# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--23_08:05:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **80,705 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 08:05:43 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.119 |  |
| 2026-02-23 08:05:38 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | -0.239 |  |
| 2026-02-23 08:05:36 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-02-23 08:04:40 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.029 |  |
| 2026-02-23 08:04:33 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:04:24 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:04:14 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.035 |  |
| 2026-02-23 08:03:46 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:03:34 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:03:31 | Peradeniya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.040 |  |
| 2026-02-23 08:03:26 | Hanwella (Kelani Ganga) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-02-23 08:03:21 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-02-23 08:02:57 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:02:41 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:02:25 | Baddegama (Gin Ganga) | 1.87 | 🟢 Normal | -0.064 |  |
| 2026-02-23 08:02:18 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-02-23 08:02:08 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.86 | 🟢 Normal | -0.100 |  |
| 2026-02-23 08:02:07 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:02:04 | Manampitiya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.986 | 🔺 Rising |
| 2026-02-23 08:01:54 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-23 08:01:51 | Weraganthota (Mahaweli Ganga) | -1.60 | 🟢 Normal | -0.021 |  |
| 2026-02-23 08:01:51 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:01:48 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:01:47 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -0.034 |  |
| 2026-02-23 08:01:46 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.020 |  |
| 2026-02-23 08:01:33 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:01:25 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | -0.021 |  |
| 2026-02-23 08:01:22 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:01:21 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:01:18 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:00:54 | Glencourse (Kelani Ganga) | 9.13 | 🟢 Normal | -0.010 |  |
| 2026-02-23 08:00:51 | Manampitiya (Mahaweli Ganga) | 2.48 | 🟢 Normal | 0.986 | 🔺 Rising |
| 2026-02-23 08:00:42 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-23 07:25:08 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | -0.064 |  |
| 2026-02-23 07:19:58 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-02-23 07:14:55 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-23 07:14:07 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | -0.095 |  |
| 2026-02-23 07:12:21 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.035 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 08:02:04 | Manampitiya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.986 | 🔺 Rising |
| 2026-02-23 08:01:54 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-23 08:03:34 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:01:22 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:01:21 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-23 07:05:28 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:01:51 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:02:57 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:01:18 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-02-23 07:00:08 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:00:42 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:02:41 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:03:46 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:04:24 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:01:48 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:02:07 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:04:33 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:01:33 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:02:08 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-02-23 08:02:18 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-02-23 08:00:54 | Glencourse (Kelani Ganga) | 9.13 | 🟢 Normal | -0.010 |  |
| 2026-02-23 07:19:58 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-02-23 08:05:36 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-02-23 08:03:21 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-02-23 08:03:26 | Hanwella (Kelani Ganga) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-02-23 08:01:46 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.020 |  |
| 2026-02-23 08:01:25 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | -0.021 |  |
| 2026-02-23 08:01:51 | Weraganthota (Mahaweli Ganga) | -1.60 | 🟢 Normal | -0.021 |  |
| 2026-02-23 08:04:40 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.029 |  |
| 2026-02-23 08:01:47 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -0.034 |  |
| 2026-02-23 08:04:14 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.035 |  |
| 2026-02-23 08:03:31 | Peradeniya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.040 |  |
| 2026-02-23 07:02:17 | Putupaula (Kalu Ganga) | 1.70 | 🟢 Normal | -0.051 |  |
| 2026-02-23 08:02:25 | Baddegama (Gin Ganga) | 1.87 | 🟢 Normal | -0.064 |  |
| 2026-02-23 07:04:21 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.068 |  |
| 2026-02-23 07:14:07 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | -0.095 |  |
| 2026-02-23 08:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.86 | 🟢 Normal | -0.100 |  |
| 2026-02-23 08:05:43 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.119 |  |
| 2026-02-23 08:05:38 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | -0.239 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)