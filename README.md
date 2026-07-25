# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--25_18:26:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **216,056 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-25 18:26:36 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:12:52 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | -0.009 |  |
| 2026-07-25 18:09:38 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:07:29 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | -0.047 |  |
| 2026-07-25 18:07:24 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:07:19 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:06:37 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-25 18:05:49 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.009 |  |
| 2026-07-25 18:05:42 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:04:48 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:04:43 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-07-25 18:04:42 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:04:19 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.140 |  |
| 2026-07-25 18:04:04 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:03:55 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-07-25 18:03:45 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:03:11 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.034 |  |
| 2026-07-25 18:02:56 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:02:53 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:02:42 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | -0.035 |  |
| 2026-07-25 18:02:36 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.013 |  |
| 2026-07-25 18:02:35 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-25 18:02:25 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-07-25 18:02:22 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-07-25 18:01:52 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.030 |  |
| 2026-07-25 18:01:49 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-07-25 18:01:48 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:01:43 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:01:43 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:01:27 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:01:21 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:01:12 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.082 |  |
| 2026-07-25 18:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:00:58 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:00:54 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:00:47 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.051 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-25 18:04:43 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-07-25 18:06:37 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-25 18:02:35 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-25 18:01:48 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:01:43 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:01:27 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:02:25 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:02:56 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-25 17:02:15 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:05:42 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:04:42 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:02:53 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-07-25 15:04:33 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:07:19 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:04:04 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:03:45 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:00:54 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:04:48 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:07:24 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:01:21 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:01:43 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:09:38 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:26:36 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:00:58 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-25 18:12:52 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | -0.009 |  |
| 2026-07-25 18:05:49 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.009 |  |
| 2026-07-25 18:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-07-25 18:03:55 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-07-25 18:02:22 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-07-25 18:01:49 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-07-25 18:02:36 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.013 |  |
| 2026-07-25 18:01:52 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.030 |  |
| 2026-07-25 18:03:11 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.034 |  |
| 2026-07-25 18:02:42 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | -0.035 |  |
| 2026-07-25 18:07:29 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | -0.047 |  |
| 2026-07-25 18:00:47 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.051 |  |
| 2026-07-25 18:01:12 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.082 |  |
| 2026-07-25 18:04:19 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.140 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)