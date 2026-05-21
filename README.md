# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--22_02:15:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **158,350 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 02:15:30 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-05-22 02:12:48 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-05-22 02:09:19 | Badalgama (Maha Oya) | 2.76 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-22 02:08:42 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-05-22 02:07:47 | Rathnapura (Kalu Ganga) | 2.43 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-05-22 02:06:44 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-22 02:06:38 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-22 02:06:31 | Glencourse (Kelani Ganga) | 10.92 | 🟢 Normal | 0.726 | 🔺 Rising |
| 2026-05-22 02:06:23 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-22 02:06:09 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-22 02:05:33 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | 0.379 | 🔺 Rising |
| 2026-05-22 02:05:23 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.270 |  |
| 2026-05-22 02:05:15 | Ellagawa (Kalu Ganga) | 5.78 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-05-22 02:05:11 | Ellagawa (Kalu Ganga) | 5.68 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-05-22 02:04:19 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-05-22 02:04:16 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-22 02:04:04 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-22 02:03:32 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-22 02:03:10 | Deraniyagala (Kelani Ganga) | 1.38 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-05-22 02:03:01 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-22 02:02:48 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-22 02:02:31 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-22 02:02:19 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-05-22 02:02:06 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-05-22 02:01:32 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-22 02:01:30 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-22 02:01:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-05-22 02:01:19 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-22 02:01:12 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:54:28 | Dunamale (Aththanagalu Oya) | 1.85 | 🟢 Normal | 0.379 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 02:05:15 | Ellagawa (Kalu Ganga) | 5.78 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-05-22 02:06:31 | Glencourse (Kelani Ganga) | 10.92 | 🟢 Normal | 0.726 | 🔺 Rising |
| 2026-05-22 02:05:33 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | 0.379 | 🔺 Rising |
| 2026-05-22 02:15:30 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-05-22 02:08:42 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-05-22 02:03:10 | Deraniyagala (Kelani Ganga) | 1.38 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-05-22 02:01:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-05-22 02:07:47 | Rathnapura (Kalu Ganga) | 2.43 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-05-22 02:04:19 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-05-22 02:09:19 | Badalgama (Maha Oya) | 2.76 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-22 02:06:09 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-22 01:32:15 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-22 02:04:16 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-21 18:16:06 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-22 02:06:44 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-22 00:07:37 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-22 02:01:12 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-22 02:01:32 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-22 02:02:48 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:03:27 | Galgamuwa (Mee Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-22 02:01:19 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-22 00:02:47 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-22 02:06:23 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-22 02:12:48 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-05-22 00:01:39 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-22 02:03:01 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-22 02:06:38 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-22 02:01:30 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-22 02:02:31 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-22 02:04:04 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-22 00:08:40 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:04:10 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.005 |  |
| 2026-05-22 02:02:19 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-05-22 01:05:02 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.019 |  |
| 2026-05-22 02:02:06 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-05-22 01:03:35 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.030 |  |
| 2026-05-21 18:01:04 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | -0.040 |  |
| 2026-05-22 01:08:11 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.066 |  |
| 2026-05-22 02:05:23 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.270 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)