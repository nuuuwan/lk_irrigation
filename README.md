# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--20_00:14:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **102,029 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 00:14:15 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 00:13:32 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-03-20 00:09:58 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-03-20 00:09:24 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-03-20 00:08:59 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-03-20 00:07:03 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.018 |  |
| 2026-03-20 00:06:41 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-03-20 00:06:23 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 00:05:40 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-03-20 00:05:11 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 00:05:10 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-20 00:04:55 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -0.044 |  |
| 2026-03-20 00:04:49 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-03-20 00:04:27 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-03-20 00:03:32 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-03-20 00:03:26 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 00:03:00 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 00:02:28 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-03-20 00:02:26 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.052 |  |
| 2026-03-20 00:02:21 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.030 |  |
| 2026-03-20 00:01:59 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-20 00:01:43 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | -0.020 |  |
| 2026-03-20 00:01:39 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-20 00:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-20 00:01:11 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-20 00:00:55 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-03-20 00:00:10 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 23:58:08 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 23:04:37 | Rathnapura (Kalu Ganga) | 2.27 | 🟢 Normal | 0.443 | 🔺 Rising |
| 2026-03-20 00:05:40 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-03-20 00:04:49 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-03-20 00:09:58 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-03-20 00:05:10 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-20 00:06:41 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-03-20 00:09:24 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-03-20 00:03:26 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 00:06:23 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 23:00:07 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 00:05:11 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 22:07:39 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-20 00:13:32 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-03-20 00:01:59 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-20 00:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-19 23:07:05 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-20 00:00:10 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:03:05 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-19 23:01:59 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-20 00:14:15 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 00:03:00 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 00:01:11 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:01:38 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 00:01:39 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-19 20:12:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-03-20 00:03:32 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-03-19 23:01:51 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-03-20 00:07:03 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.018 |  |
| 2026-03-20 00:04:27 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-03-20 00:00:55 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-03-20 00:02:28 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-03-20 00:01:43 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | -0.020 |  |
| 2026-03-20 00:08:59 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-03-20 00:02:21 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.030 |  |
| 2026-03-20 00:04:55 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -0.044 |  |
| 2026-03-19 22:04:21 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.049 |  |
| 2026-03-20 00:02:26 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.052 |  |
| 2026-03-19 18:02:05 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.128 |  |
| 2026-03-19 21:09:33 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.134 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)