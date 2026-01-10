# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--10_11:06:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **41,720 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 11:06:48 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-10 11:06:29 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-10 11:05:39 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.120 |  |
| 2026-01-10 11:05:34 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-10 11:05:10 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-01-10 11:04:45 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-01-10 11:04:31 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-10 11:04:12 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.061 |  |
| 2026-01-10 11:04:04 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-01-10 11:04:00 | Katharagama (Menik Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-10 11:04:00 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-10 11:03:33 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-10 11:03:20 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.063 |  |
| 2026-01-10 11:03:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.39 | 🟢 Normal | -0.039 |  |
| 2026-01-10 11:03:11 | Padiyathalawa (Maduru Oya) | 1.27 | 🟢 Normal | -0.051 |  |
| 2026-01-10 11:02:58 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-10 11:02:52 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.058 |  |
| 2026-01-10 11:02:49 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-10 11:02:25 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-10 11:02:23 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.050 |  |
| 2026-01-10 11:02:09 | Weraganthota (Mahaweli Ganga) | -1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-10 11:01:48 | Yaka Wewa (Ma Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-10 11:01:45 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-10 11:01:40 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-01-10 11:01:27 | Moragaswewa (Deduru Oya) | 0.72 | 🟢 Normal | -0.052 |  |
| 2026-01-10 11:01:22 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-01-10 11:00:37 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-10 11:00:30 | Horowpothana (Yan Oya) | 2.71 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-10 10:30:21 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-10 10:27:03 | Moragaswewa (Deduru Oya) | 0.75 | 🟢 Normal | -0.052 |  |
| 2026-01-10 10:16:15 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-10 10:16:10 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-10 10:16:06 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-10 10:14:17 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-10 10:11:07 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 10:06:00 | Peradeniya (Mahaweli Ganga) | 2.07 | 🟢 Normal | 0.328 | 🔺 Rising |
| 2026-01-10 11:00:30 | Horowpothana (Yan Oya) | 2.71 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-10 10:08:43 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-10 10:07:01 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 11:02:09 | Weraganthota (Mahaweli Ganga) | -1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-10 11:04:00 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-10 11:06:48 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-10 11:01:48 | Yaka Wewa (Ma Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-10 11:06:29 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-10 10:16:15 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-10 10:16:10 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-10 11:02:58 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-10 11:01:45 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-10 11:02:49 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-10 10:04:18 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:05:43 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-10 11:04:31 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-10 11:02:25 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-10 11:04:00 | Katharagama (Menik Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-10 11:00:37 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-10 10:00:49 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 11:03:33 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-10 11:05:34 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-10 10:30:21 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-10 09:08:13 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | -0.005 |  |
| 2026-01-10 11:04:04 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-01-10 11:01:40 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-01-10 11:04:45 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-01-10 11:05:10 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-01-10 10:04:02 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-01-10 11:01:22 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-01-10 11:03:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.39 | 🟢 Normal | -0.039 |  |
| 2026-01-10 11:02:23 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.050 |  |
| 2026-01-10 11:03:11 | Padiyathalawa (Maduru Oya) | 1.27 | 🟢 Normal | -0.051 |  |
| 2026-01-10 11:01:27 | Moragaswewa (Deduru Oya) | 0.72 | 🟢 Normal | -0.052 |  |
| 2026-01-10 11:02:52 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.058 |  |
| 2026-01-10 11:04:12 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.061 |  |
| 2026-01-10 11:03:20 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.063 |  |
| 2026-01-10 11:05:39 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)