# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--13_04:23:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **95,908 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 04:23:12 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:15:04 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-03-13 04:12:46 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-03-13 04:11:14 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:08:45 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-13 04:08:32 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:08:03 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.028 |  |
| 2026-03-13 04:07:36 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -36.000 |  |
| 2026-03-13 04:07:35 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -36.000 |  |
| 2026-03-13 04:07:20 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-03-13 04:07:16 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:06:40 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:06:29 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:06:28 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:06:11 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.051 |  |
| 2026-03-13 04:06:06 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.030 |  |
| 2026-03-13 04:05:02 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:05:00 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.120 |  |
| 2026-03-13 04:04:45 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.552 | 🔺 Rising |
| 2026-03-13 04:04:25 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:04:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-03-13 04:03:57 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-03-13 04:03:26 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.062 |  |
| 2026-03-13 04:03:14 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:03:09 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:02:48 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-13 04:02:22 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.328 | 🔺 Rising |
| 2026-03-13 04:02:12 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:02:11 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:01:58 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:01:55 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:01:43 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-03-13 04:01:40 | Manampitiya (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-03-13 04:00:22 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 04:00:11 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:00:06 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 04:04:45 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.552 | 🔺 Rising |
| 2026-03-13 04:02:22 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.328 | 🔺 Rising |
| 2026-03-13 04:15:04 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-03-13 04:01:43 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-03-13 04:03:57 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-03-13 04:12:46 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-03-13 04:08:45 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-13 04:04:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-03-13 04:02:48 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-13 04:00:22 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 04:00:11 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:07:16 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:02:17 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:00:06 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:05:52 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:03:09 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:01:58 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:05:30 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:23:12 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-03-13 03:02:58 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:06:29 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:06:40 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:08:32 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:11:14 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:03:14 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:05:02 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:03:01 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:04:25 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:01:55 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:02:11 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-13 04:07:20 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-03-13 04:01:40 | Manampitiya (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-03-13 04:08:03 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.028 |  |
| 2026-03-13 04:06:06 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.030 |  |
| 2026-03-13 04:06:11 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.051 |  |
| 2026-03-13 04:03:26 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.062 |  |
| 2026-03-12 18:02:28 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.083 |  |
| 2026-03-13 04:05:00 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.120 |  |
| 2026-03-13 04:07:36 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)