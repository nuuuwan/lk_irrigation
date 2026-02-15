# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--16_05:11:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **74,307 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-16 05:11:56 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.060 |  |
| 2026-02-16 05:10:47 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-02-16 05:09:50 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.018 |  |
| 2026-02-16 05:08:10 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-02-16 05:07:28 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-16 05:06:27 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-16 05:06:10 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -0.096 |  |
| 2026-02-16 05:06:09 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-02-16 05:05:43 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | -0.005 |  |
| 2026-02-16 05:05:37 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-16 05:05:08 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-02-16 05:05:07 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | -0.019 |  |
| 2026-02-16 05:04:46 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-16 05:04:06 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-02-16 05:04:01 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-02-16 05:03:54 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-16 05:03:25 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-16 05:03:13 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-16 05:02:47 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-16 05:02:36 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-16 05:02:34 | Manampitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.067 |  |
| 2026-02-16 05:01:45 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-16 05:01:38 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-16 05:01:36 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.050 |  |
| 2026-02-16 05:01:26 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-16 05:01:14 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.030 |  |
| 2026-02-16 05:01:09 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.003 |  |
| 2026-02-16 05:01:04 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.578 | 🔺 Rising |
| 2026-02-16 05:00:53 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-16 05:00:39 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-02-16 05:00:18 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-16 05:00:17 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-02-16 04:34:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-16 04:28:48 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.096 |  |
| 2026-02-16 04:26:41 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-16 05:01:04 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.578 | 🔺 Rising |
| 2026-02-16 05:00:39 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-02-16 05:04:01 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-02-16 04:04:32 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-02-16 05:07:28 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-16 04:34:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-16 05:04:06 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-02-16 05:05:37 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-16 05:00:18 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-16 04:07:35 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.005 |  |
| 2026-02-16 04:06:12 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.004 |  |
| 2026-02-16 05:01:09 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.003 |  |
| 2026-02-16 05:03:13 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-16 05:01:26 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-16 05:01:45 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-16 05:02:36 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:02:48 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-16 05:06:09 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-02-16 05:00:53 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-16 05:03:54 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-16 05:08:10 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-02-16 05:01:38 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-16 05:02:47 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-16 05:04:46 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-16 05:03:25 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-16 05:06:27 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:01:14 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-02-16 05:10:47 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-02-16 05:05:43 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | -0.005 |  |
| 2026-02-16 05:05:08 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-02-16 05:00:17 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-02-16 05:09:50 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.018 |  |
| 2026-02-16 05:05:07 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | -0.019 |  |
| 2026-02-16 05:01:14 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.030 |  |
| 2026-02-16 05:01:36 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.050 |  |
| 2026-02-16 05:11:56 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.060 |  |
| 2026-02-15 18:00:16 | Weraganthota (Mahaweli Ganga) | -2.47 | 🟢 Normal | -0.064 |  |
| 2026-02-16 05:02:34 | Manampitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.067 |  |
| 2026-02-16 05:06:10 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)