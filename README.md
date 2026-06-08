# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--08_10:16:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **173,694 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 10:16:22 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.018 |  |
| 2026-06-08 10:15:25 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-08 10:15:10 | Baddegama (Gin Ganga) | 2.72 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-08 10:09:57 | Peradeniya (Mahaweli Ganga) | 2.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-08 10:08:38 | Deraniyagala (Kelani Ganga) | 1.28 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-08 10:08:21 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-08 10:08:10 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-08 10:08:08 | Badalgama (Maha Oya) | 2.99 | 🟢 Normal | -0.010 |  |
| 2026-06-08 10:07:49 | Magura (Kalu Ganga) | 2.75 | 🟢 Normal | -0.030 |  |
| 2026-06-08 10:07:40 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 10:07:38 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-06-08 10:06:59 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.027 |  |
| 2026-06-08 10:05:43 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-06-08 10:05:42 | Rathnapura (Kalu Ganga) | 2.96 | 🟢 Normal | -0.058 |  |
| 2026-06-08 10:05:36 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.067 |  |
| 2026-06-08 10:05:02 | Panadugama (Nilwala Ganga) | 3.40 | 🟢 Normal | 0.000 |  |
| 2026-06-08 10:04:33 | Putupaula (Kalu Ganga) | 1.85 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-08 10:04:24 | Glencourse (Kelani Ganga) | 11.16 | 🟢 Normal | -0.062 |  |
| 2026-06-08 10:04:16 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-06-08 10:04:09 | Hanwella (Kelani Ganga) | 3.42 | 🟢 Normal | -0.059 |  |
| 2026-06-08 10:04:01 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-08 10:03:53 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-06-08 10:03:27 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 10:03:23 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.114 |  |
| 2026-06-08 10:03:02 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-08 10:02:55 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-08 10:02:53 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-08 10:02:32 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | -0.020 |  |
| 2026-06-08 10:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.00 | 🟡 Alert | -0.050 |  |
| 2026-06-08 10:02:10 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.030 |  |
| 2026-06-08 10:02:01 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-08 10:02:01 | Ellagawa (Kalu Ganga) | 7.57 | 🟢 Normal | -0.010 |  |
| 2026-06-08 10:01:45 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-08 10:01:01 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-08 10:00:55 | Nawalapitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.020 |  |
| 2026-06-08 10:00:55 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-08 10:00:38 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-08 10:00:22 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-08 10:00:13 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 10:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.00 | 🟡 Alert | -0.050 |  |
| 2026-06-08 10:04:33 | Putupaula (Kalu Ganga) | 1.85 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-08 10:08:21 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-08 10:15:25 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-08 10:08:38 | Deraniyagala (Kelani Ganga) | 1.28 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-08 10:01:45 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-08 10:00:55 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-08 10:03:27 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 10:09:57 | Peradeniya (Mahaweli Ganga) | 2.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-08 10:08:10 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-08 10:15:10 | Baddegama (Gin Ganga) | 2.72 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-08 10:00:22 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-08 10:04:01 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-08 10:02:55 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-08 10:00:38 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-08 10:05:02 | Panadugama (Nilwala Ganga) | 3.40 | 🟢 Normal | 0.000 |  |
| 2026-06-08 10:07:40 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 10:03:53 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-06-08 10:02:53 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-08 10:03:02 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-08 10:02:01 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-08 10:01:01 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-08 10:05:43 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-06-08 10:07:38 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-06-08 10:08:08 | Badalgama (Maha Oya) | 2.99 | 🟢 Normal | -0.010 |  |
| 2026-06-08 10:04:16 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-06-08 10:02:01 | Ellagawa (Kalu Ganga) | 7.57 | 🟢 Normal | -0.010 |  |
| 2026-06-08 10:00:13 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-06-08 10:16:22 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.018 |  |
| 2026-06-08 10:00:55 | Nawalapitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.020 |  |
| 2026-06-08 10:02:32 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | -0.020 |  |
| 2026-06-08 10:06:59 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.027 |  |
| 2026-06-08 10:02:10 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.030 |  |
| 2026-06-08 10:07:49 | Magura (Kalu Ganga) | 2.75 | 🟢 Normal | -0.030 |  |
| 2026-06-08 10:05:42 | Rathnapura (Kalu Ganga) | 2.96 | 🟢 Normal | -0.058 |  |
| 2026-06-08 10:04:09 | Hanwella (Kelani Ganga) | 3.42 | 🟢 Normal | -0.059 |  |
| 2026-06-08 10:04:24 | Glencourse (Kelani Ganga) | 11.16 | 🟢 Normal | -0.062 |  |
| 2026-06-08 10:05:36 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.067 |  |
| 2026-06-08 10:03:23 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.114 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)