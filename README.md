# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--16_02:47:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **74,211 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-16 02:47:27 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-02-16 02:41:40 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:41:10 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:19:19 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:14:55 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | -0.004 |  |
| 2026-02-16 02:13:05 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:09:37 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-02-16 02:07:04 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:06:44 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.005 |  |
| 2026-02-16 02:06:07 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | -0.010 |  |
| 2026-02-16 02:06:01 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:05:57 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:05:37 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:04:33 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:04:14 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:04:09 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:03:53 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-02-16 02:03:47 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-16 02:03:06 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.195 |  |
| 2026-02-16 02:02:45 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | -0.005 |  |
| 2026-02-16 02:02:42 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:02:18 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:02:13 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-02-16 02:01:36 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:01:14 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | -0.021 |  |
| 2026-02-16 02:01:10 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:01:07 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-16 02:01:05 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:01:04 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:00:48 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-02-16 02:00:45 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-02-16 02:00:42 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:00:27 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-16 02:09:37 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-02-16 02:02:13 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-02-16 02:01:07 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-16 02:03:47 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-16 02:47:27 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-02-16 01:44:25 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-02-16 02:06:44 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.005 |  |
| 2026-02-16 02:01:36 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:02:18 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:00:27 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:13:05 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:04:14 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:02:48 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:01:05 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:07:04 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:00:42 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:02:42 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:04:09 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:05:37 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:05:57 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:19:19 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:04:33 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:01:14 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:41:40 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:01:10 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:06:01 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-16 02:14:55 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | -0.004 |  |
| 2026-02-16 00:07:06 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | -0.005 |  |
| 2026-02-16 02:02:45 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | -0.005 |  |
| 2026-02-16 02:06:07 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | -0.010 |  |
| 2026-02-16 02:03:53 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-02-16 02:00:48 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-02-16 02:00:45 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-02-16 01:45:27 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.015 |  |
| 2026-02-16 02:01:14 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | -0.021 |  |
| 2026-02-16 00:04:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.027 |  |
| 2026-02-16 01:00:52 | Manampitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.050 |  |
| 2026-02-15 18:00:16 | Weraganthota (Mahaweli Ganga) | -2.47 | 🟢 Normal | -0.064 |  |
| 2026-02-16 02:03:06 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.195 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)