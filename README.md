# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--10_02:43:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **68,850 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-10 02:43:25 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-10 02:16:46 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -36.000 |  |
| 2026-02-10 02:16:45 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -36.000 |  |
| 2026-02-10 02:16:44 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -36.000 |  |
| 2026-02-10 02:16:42 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -36.000 |  |
| 2026-02-10 02:13:11 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-10 02:11:02 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-10 02:06:55 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-10 02:06:26 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-10 02:06:15 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-10 02:06:11 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-10 02:05:51 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-10 02:05:27 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-02-10 02:04:41 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-10 02:04:40 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-10 02:04:36 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.004 |  |
| 2026-02-10 02:04:28 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-10 02:04:19 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.030 |  |
| 2026-02-10 02:02:59 | Peradeniya (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.128 |  |
| 2026-02-10 02:02:59 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-10 02:02:52 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-10 02:02:45 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-10 02:02:42 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-10 02:02:10 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-10 02:02:07 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-02-10 02:02:04 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-02-10 02:02:02 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-10 02:01:51 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-02-10 02:01:43 | Manampitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-02-10 02:01:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-02-10 02:01:28 | Dunamale (Aththanagalu Oya) | 0.13 | 🟢 Normal | -0.874 |  |
| 2026-02-10 02:01:20 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-10 02:01:08 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-10 02:02:04 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-02-10 02:04:40 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-10 01:02:10 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-10 02:01:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-02-10 02:05:27 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-02-10 02:04:28 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-10 02:02:10 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-10 02:06:15 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-10 02:04:36 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.004 |  |
| 2026-02-10 01:40:58 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-10 02:02:59 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-10 02:43:25 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-10 02:02:52 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-10 02:13:11 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-09 18:02:36 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-10 01:21:51 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-10 02:11:02 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-10 01:48:58 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-10 01:29:55 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | 0.000 |  |
| 2026-02-10 02:02:45 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-10 02:02:02 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-10 02:01:20 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-10 02:06:55 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-10 02:04:41 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-10 02:06:11 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-10 00:02:41 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-10 02:06:26 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-10 02:01:08 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | -0.010 |  |
| 2026-02-10 02:01:51 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-02-09 18:00:27 | Thanthirimale (Malwathu Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-02-10 02:02:07 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-02-09 20:18:59 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.019 |  |
| 2026-02-10 02:04:19 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.030 |  |
| 2026-02-10 02:01:43 | Manampitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-02-09 18:01:51 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.080 |  |
| 2026-02-09 23:06:15 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.108 |  |
| 2026-02-10 02:02:59 | Peradeniya (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.128 |  |
| 2026-02-10 02:01:28 | Dunamale (Aththanagalu Oya) | 0.13 | 🟢 Normal | -0.874 |  |
| 2026-02-10 02:16:46 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)