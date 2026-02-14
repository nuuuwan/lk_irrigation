# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--15_02:22:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **73,320 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 02:22:05 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.003 |  |
| 2026-02-15 02:12:46 | Glencourse (Kelani Ganga) | 8.29 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-02-15 02:09:34 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-15 02:08:58 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-02-15 02:08:54 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-15 02:07:29 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -0.057 |  |
| 2026-02-15 02:07:21 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 02:07:01 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | -0.005 |  |
| 2026-02-15 02:05:13 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-15 02:04:54 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-15 02:04:15 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-15 02:04:09 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-02-15 02:03:19 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-15 02:03:17 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 02:02:57 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 2.687 | 🔺 Rising |
| 2026-02-15 02:02:50 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-15 02:02:25 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | -0.011 |  |
| 2026-02-15 02:02:23 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 02:02:14 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-15 02:01:50 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 2.687 | 🔺 Rising |
| 2026-02-15 02:01:46 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-15 02:01:38 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-15 02:01:36 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-15 02:01:26 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-15 02:01:13 | Peradeniya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.090 |  |
| 2026-02-15 02:00:50 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 02:00:26 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 02:02:57 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 2.687 | 🔺 Rising |
| 2026-02-15 00:10:59 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-02-15 00:07:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-02-15 02:08:58 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-02-15 00:00:48 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-02-15 02:08:54 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-15 02:03:19 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-15 00:07:32 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-15 02:12:46 | Glencourse (Kelani Ganga) | 8.29 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-02-15 02:02:50 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-15 02:02:23 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 02:03:17 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 02:00:50 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 01:04:13 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 22:00:48 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 18:02:04 | Weraganthota (Mahaweli Ganga) | -1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 02:07:21 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 02:05:13 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-15 02:02:14 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-15 02:01:38 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:03:27 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-15 01:02:47 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-02-15 01:07:25 | Padiyathalawa (Maduru Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-02-15 02:00:26 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-15 02:09:34 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-15 01:02:33 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 01:01:09 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-15 02:01:36 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:01:28 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-02-15 02:04:54 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-15 02:04:15 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-15 02:01:26 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-15 02:01:46 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-15 02:22:05 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.003 |  |
| 2026-02-15 02:07:01 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | -0.005 |  |
| 2026-02-15 02:04:09 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-02-15 02:02:25 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | -0.011 |  |
| 2026-02-15 02:07:29 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -0.057 |  |
| 2026-02-15 02:01:13 | Peradeniya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)