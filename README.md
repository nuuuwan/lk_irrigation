# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--27_01:03:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **190,315 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 01:03:20 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:02:46 | Glencourse (Kelani Ganga) | 10.14 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-06-27 01:02:45 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-06-27 01:02:31 | Peradeniya (Mahaweli Ganga) | 2.14 | 🟢 Normal | -0.126 |  |
| 2026-06-27 01:02:22 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:02:19 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:01:37 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 01:01:36 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-06-27 01:01:36 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-27 01:01:09 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:01:05 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:00:46 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.385 | 🔺 Rising |
| 2026-06-27 00:57:39 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.385 | 🔺 Rising |
| 2026-06-27 00:44:54 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-27 00:38:17 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 00:20:31 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 00:14:52 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 01:00:46 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.385 | 🔺 Rising |
| 2026-06-27 00:06:39 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-06-27 01:02:46 | Glencourse (Kelani Ganga) | 10.14 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-06-27 01:01:36 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-27 00:02:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.92 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-27 00:06:23 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-26 22:07:10 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-27 00:04:30 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 01:01:37 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 18:00:54 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:01:05 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 00:09:19 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-27 00:20:31 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:03:20 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:01:09 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-26 18:06:01 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-27 00:04:50 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-27 00:08:13 | Hanwella (Kelani Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-06-27 00:14:52 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-27 00:07:33 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-06-27 00:44:54 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:02:19 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-27 00:04:23 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-26 18:02:53 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-27 00:07:58 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-06-27 01:02:22 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-27 00:03:12 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-27 00:09:08 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.005 |  |
| 2026-06-27 00:05:59 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-06-27 01:02:45 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-06-27 01:01:36 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-06-27 00:01:57 | Dunamale (Aththanagalu Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-06-27 00:01:39 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.011 |  |
| 2026-06-27 00:01:35 | Rathnapura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.012 |  |
| 2026-06-27 00:02:04 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.019 |  |
| 2026-06-27 00:08:53 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.025 |  |
| 2026-06-27 00:08:53 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | -0.058 |  |
| 2026-06-27 01:02:31 | Peradeniya (Mahaweli Ganga) | 2.14 | 🟢 Normal | -0.126 |  |
| 2026-06-27 00:05:44 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.181 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)