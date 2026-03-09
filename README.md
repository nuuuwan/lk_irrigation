# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--10_02:20:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **93,949 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-10 02:20:11 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | -0.006 |  |
| 2026-03-10 02:12:09 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:11:47 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:11:31 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:10:14 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.061 |  |
| 2026-03-10 02:08:18 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-03-10 02:08:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-03-10 02:07:56 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | -0.089 |  |
| 2026-03-10 02:07:01 | Dunamale (Aththanagalu Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:05:56 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-03-10 02:05:55 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.011 |  |
| 2026-03-10 02:05:43 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-03-10 02:05:37 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:05:30 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-03-10 02:05:18 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:04:53 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:04:19 | Manampitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.050 |  |
| 2026-03-10 02:04:19 | Thawalama (Gin Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:04:13 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.020 |  |
| 2026-03-10 02:03:54 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:03:35 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:02:40 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:02:37 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:02:23 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-10 02:02:05 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-03-10 02:01:58 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-10 02:01:49 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.441 | 🔺 Rising |
| 2026-03-10 02:01:47 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-03-10 02:01:35 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:01:33 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:01:27 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:01:20 | Thalgahagoda (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.020 |  |
| 2026-03-10 02:01:19 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | -0.040 |  |
| 2026-03-10 02:01:15 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:01:03 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-10 01:59:43 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-10 01:44:28 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.035 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-10 02:01:49 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.441 | 🔺 Rising |
| 2026-03-09 18:01:06 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-03-10 02:05:43 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-03-10 02:08:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-03-10 02:01:58 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-10 02:01:47 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-03-10 00:08:18 | Putupaula (Kalu Ganga) | 0.19 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-10 02:08:18 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-03-09 22:02:21 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-03-10 02:02:23 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-10 01:07:52 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 02:01:15 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:04:53 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:01:35 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:01:27 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-09 18:06:39 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:11:47 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:01:03 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:02:37 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:07:01 | Dunamale (Aththanagalu Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:05:37 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:01:33 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:03:35 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:04:19 | Thawalama (Gin Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:05:18 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:02:40 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:12:09 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-10 02:20:11 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | -0.006 |  |
| 2026-03-10 02:05:30 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-03-10 02:02:05 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-03-10 02:05:55 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.011 |  |
| 2026-03-10 02:04:13 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.020 |  |
| 2026-03-10 02:05:56 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-03-10 02:01:20 | Thalgahagoda (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.020 |  |
| 2026-03-10 02:01:19 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | -0.040 |  |
| 2026-03-10 02:04:19 | Manampitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.050 |  |
| 2026-03-10 02:10:14 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.061 |  |
| 2026-03-09 18:01:53 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | -0.075 |  |
| 2026-03-10 02:07:56 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)