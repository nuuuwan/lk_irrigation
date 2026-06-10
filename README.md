# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--11_01:42:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **176,025 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 01:42:37 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -18.000 |  |
| 2026-06-11 01:42:35 | Magura (Kalu Ganga) | 2.01 | 🟢 Normal | -18.000 |  |
| 2026-06-11 01:37:22 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.013 |  |
| 2026-06-11 01:27:12 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-06-11 01:26:51 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-11 01:26:24 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.004 |  |
| 2026-06-11 01:20:13 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-11 01:13:04 | Glencourse (Kelani Ganga) | 10.68 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-06-11 01:10:33 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-11 01:10:13 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-11 01:09:49 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.210 |  |
| 2026-06-11 01:07:08 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-06-11 01:06:13 | Nawalapitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-11 01:06:03 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | -0.010 |  |
| 2026-06-11 01:05:42 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-11 01:04:21 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | -0.019 |  |
| 2026-06-11 01:04:04 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 01:03:56 | Hanwella (Kelani Ganga) | 2.45 | 🟢 Normal | -0.011 |  |
| 2026-06-11 01:03:51 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-11 01:03:38 | Rathnapura (Kalu Ganga) | 1.85 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-06-11 01:03:03 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-11 01:02:52 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-11 01:02:39 | Manampitiya (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-11 01:02:28 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-11 01:02:17 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-11 01:01:25 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-11 01:01:10 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.069 |  |
| 2026-06-11 01:00:49 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-11 01:00:26 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-11 01:00:23 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 01:13:04 | Glencourse (Kelani Ganga) | 10.68 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-06-11 01:03:38 | Rathnapura (Kalu Ganga) | 1.85 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-06-11 01:06:13 | Nawalapitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-11 01:02:17 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-11 01:02:39 | Manampitiya (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-10 23:03:31 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-11 01:26:24 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.004 |  |
| 2026-06-11 01:07:08 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-06-11 01:00:23 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-11 01:00:49 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-11 01:03:03 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:11:52 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 01:01:25 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-11 01:00:26 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-10 18:03:48 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-11 01:10:33 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-11 01:02:28 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:07:23 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-11 01:10:13 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-11 01:02:52 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:02:17 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-11 01:04:04 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 00:09:37 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-11 01:26:51 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-10 18:23:24 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-11 01:20:13 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-11 01:05:42 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-10 23:21:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.51 | 🟢 Normal | -0.008 |  |
| 2026-06-11 01:06:03 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | -0.010 |  |
| 2026-06-11 01:03:51 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-11 00:05:37 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-06-11 01:27:12 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-06-11 01:03:56 | Hanwella (Kelani Ganga) | 2.45 | 🟢 Normal | -0.011 |  |
| 2026-06-11 01:37:22 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.013 |  |
| 2026-06-11 01:04:21 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | -0.019 |  |
| 2026-06-10 18:01:23 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.020 |  |
| 2026-06-11 01:01:10 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.069 |  |
| 2026-06-11 01:09:49 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.210 |  |
| 2026-06-11 01:42:37 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)