# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_13:18:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **172,030 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 13:18:32 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.017 |  |
| 2026-06-06 13:09:10 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | -0.009 |  |
| 2026-06-06 13:08:26 | Dunamale (Aththanagalu Oya) | 3.18 | 🟢 Normal | -0.018 |  |
| 2026-06-06 13:08:21 | Peradeniya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.018 |  |
| 2026-06-06 13:08:06 | Putupaula (Kalu Ganga) | 1.50 | 🟢 Normal | -0.027 |  |
| 2026-06-06 13:08:03 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-06 13:07:56 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-06-06 13:07:50 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-06-06 13:07:22 | Baddegama (Gin Ganga) | 1.99 | 🟢 Normal | -0.019 |  |
| 2026-06-06 13:07:12 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 13:06:32 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-06 13:06:19 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.068 |  |
| 2026-06-06 13:05:19 | Glencourse (Kelani Ganga) | 11.28 | 🟢 Normal | -0.041 |  |
| 2026-06-06 13:05:12 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.058 |  |
| 2026-06-06 13:05:07 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-06-06 13:04:19 | Rathnapura (Kalu Ganga) | 3.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 13:04:17 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-06-06 13:04:01 | Deraniyagala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.040 |  |
| 2026-06-06 13:03:52 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-06 13:03:52 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-06 13:03:50 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-06-06 13:03:36 | Ellagawa (Kalu Ganga) | 7.33 | 🟢 Normal | -0.010 |  |
| 2026-06-06 13:03:15 | Hanwella (Kelani Ganga) | 3.51 | 🟢 Normal | -0.050 |  |
| 2026-06-06 13:03:01 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-06-06 13:03:01 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-06-06 13:02:35 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 13:02:31 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.031 |  |
| 2026-06-06 13:02:28 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-06 13:02:25 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-06-06 13:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.27 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 12:04:38 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-06 13:08:03 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-06 13:04:19 | Rathnapura (Kalu Ganga) | 3.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 13:07:12 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 12:01:20 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-06-06 13:00:39 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 13:00:15 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-06 13:03:52 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-06 13:03:01 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-06-06 13:02:35 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 13:06:32 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-06 13:02:28 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-06 13:04:17 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | 0.000 |  |
| 2026-06-06 13:01:47 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-06 12:01:24 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-06 13:03:52 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-06 13:09:10 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | -0.009 |  |
| 2026-06-06 13:05:07 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-06-06 13:07:50 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-06-06 13:07:56 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-06-06 13:03:36 | Ellagawa (Kalu Ganga) | 7.33 | 🟢 Normal | -0.010 |  |
| 2026-06-06 13:03:50 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-06-06 13:02:25 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-06-06 13:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.27 | 🟢 Normal | -0.010 |  |
| 2026-06-06 13:01:33 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -0.010 |  |
| 2026-06-06 13:01:25 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-06-06 13:18:32 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.017 |  |
| 2026-06-06 13:08:21 | Peradeniya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.018 |  |
| 2026-06-06 13:08:26 | Dunamale (Aththanagalu Oya) | 3.18 | 🟢 Normal | -0.018 |  |
| 2026-06-06 13:07:22 | Baddegama (Gin Ganga) | 1.99 | 🟢 Normal | -0.019 |  |
| 2026-06-06 13:03:01 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-06-06 13:08:06 | Putupaula (Kalu Ganga) | 1.50 | 🟢 Normal | -0.027 |  |
| 2026-06-06 13:02:31 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.031 |  |
| 2026-06-06 12:04:23 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | -0.031 |  |
| 2026-06-06 13:04:01 | Deraniyagala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.040 |  |
| 2026-06-06 13:05:19 | Glencourse (Kelani Ganga) | 11.28 | 🟢 Normal | -0.041 |  |
| 2026-06-06 13:03:15 | Hanwella (Kelani Ganga) | 3.51 | 🟢 Normal | -0.050 |  |
| 2026-06-06 13:05:12 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.058 |  |
| 2026-06-06 13:06:19 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.068 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)