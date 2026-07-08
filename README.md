# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--08_05:35:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **200,340 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-08 05:35:37 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:28:10 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.025 |  |
| 2026-07-08 05:27:37 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:25:39 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.007 |  |
| 2026-07-08 05:18:55 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | -36.000 |  |
| 2026-07-08 05:18:54 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | -36.000 |  |
| 2026-07-08 05:18:52 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | -36.000 |  |
| 2026-07-08 05:15:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | -0.066 |  |
| 2026-07-08 05:15:15 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-08 05:07:00 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-07-08 05:06:20 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:06:17 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-08 05:05:41 | Glencourse (Kelani Ganga) | 9.66 | 🟢 Normal | -0.043 |  |
| 2026-07-08 05:05:32 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:05:14 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:04:40 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:04:12 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-08 05:03:59 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-08 05:03:40 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:03:01 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-07-08 05:02:58 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | -0.010 |  |
| 2026-07-08 05:02:55 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:02:37 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-07-08 05:02:36 | Hanwella (Kelani Ganga) | 1.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-08 05:02:25 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:02:18 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:01:41 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:01:36 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:01:30 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-08 05:01:24 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | -18.000 |  |
| 2026-07-08 05:01:22 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -18.000 |  |
| 2026-07-08 05:01:11 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:01:10 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:01:09 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:00:45 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-08 05:00:45 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-08 04:59:34 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.041 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-08 04:03:17 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-07-08 05:03:59 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-08 05:00:45 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-08 05:01:30 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-08 05:06:17 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-08 05:15:15 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-08 05:02:36 | Hanwella (Kelani Ganga) | 1.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-08 05:04:12 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-08 04:12:18 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-07 18:04:20 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:00:45 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:01:10 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:02:55 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:01:36 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:01:41 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:02:25 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:05:14 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:03:00 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:06:20 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:05:32 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:01:09 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:02:18 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:01:11 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:04:40 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:35:37 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:01:02 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:03:40 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:27:37 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-08 05:25:39 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.007 |  |
| 2026-07-08 05:07:00 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-07-08 05:02:58 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | -0.010 |  |
| 2026-07-08 05:03:01 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-07-08 05:02:37 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-07-08 05:28:10 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.025 |  |
| 2026-07-08 04:59:34 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.041 |  |
| 2026-07-08 05:05:41 | Glencourse (Kelani Ganga) | 9.66 | 🟢 Normal | -0.043 |  |
| 2026-07-08 05:15:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | -0.066 |  |
| 2026-07-08 05:01:24 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | -18.000 |  |
| 2026-07-08 05:18:55 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)