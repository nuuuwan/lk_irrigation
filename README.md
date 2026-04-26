# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--27_02:20:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **136,041 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 02:20:00 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -1.204 |  |
| 2026-04-27 02:14:36 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:14:14 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:13:53 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:09:22 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-04-27 02:08:24 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-04-27 02:08:09 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:08:08 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:08:01 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-04-27 02:07:30 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-27 02:06:40 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:05:27 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:03:20 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-27 02:03:18 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.304 | 🔺 Rising |
| 2026-04-27 02:03:16 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:03:06 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.079 |  |
| 2026-04-27 02:02:40 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:02:38 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:02:23 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:02:21 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:02:20 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:02:11 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:01:55 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:01:35 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 02:01:34 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.020 |  |
| 2026-04-27 02:01:33 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-04-27 02:01:25 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:01:19 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:01:17 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:01:15 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-27 02:01:03 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-27 01:49:44 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.193 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 02:03:18 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.304 | 🔺 Rising |
| 2026-04-27 02:08:24 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-04-27 02:08:01 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-04-27 02:03:20 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-27 01:07:06 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-27 01:03:33 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-27 02:07:30 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-27 02:01:15 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-27 02:01:35 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-26 18:00:28 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:02:23 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:01:25 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 01:35:58 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:02:38 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:01:55 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:08:09 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:02:11 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:01:17 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:01:19 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:03:16 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:14:14 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:14:36 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:01:03 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:06:40 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:05:27 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-27 01:25:59 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-27 02:02:40 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-27 00:09:01 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | -0.005 |  |
| 2026-04-27 00:23:01 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | -0.008 |  |
| 2026-04-27 02:09:22 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-04-26 18:06:09 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.009 |  |
| 2026-04-27 02:01:33 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-04-27 02:01:34 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.020 |  |
| 2026-04-26 18:03:51 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.029 |  |
| 2026-04-27 01:02:07 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.055 |  |
| 2026-04-27 01:18:57 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.061 |  |
| 2026-04-27 02:03:06 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.079 |  |
| 2026-04-26 20:08:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.123 |  |
| 2026-04-27 02:20:00 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -1.204 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)