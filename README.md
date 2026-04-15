# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_08:06:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **125,544 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 08:06:37 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | -0.009 |  |
| 2026-04-15 08:06:29 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.060 |  |
| 2026-04-15 08:05:36 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | -0.014 |  |
| 2026-04-15 08:05:18 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.012 |  |
| 2026-04-15 08:04:55 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-15 08:04:40 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.109 |  |
| 2026-04-15 08:04:27 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | -0.039 |  |
| 2026-04-15 08:04:24 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | -0.011 |  |
| 2026-04-15 08:04:04 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.066 |  |
| 2026-04-15 08:04:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.088 |  |
| 2026-04-15 08:03:42 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-15 08:03:38 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-15 08:03:21 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | -0.049 |  |
| 2026-04-15 08:03:15 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 08:02:59 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.050 |  |
| 2026-04-15 08:02:52 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-04-15 08:02:44 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-15 08:02:41 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-15 08:02:30 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.022 |  |
| 2026-04-15 08:02:25 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 08:02:20 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-15 08:02:14 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-04-15 08:02:07 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-15 08:01:55 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-15 08:01:54 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-04-15 08:01:50 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-04-15 08:01:40 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 08:01:08 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.139 |  |
| 2026-04-15 08:01:04 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-15 08:00:49 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-04-15 08:00:47 | Thanthirimale (Malwathu Oya) | 2.78 | 🟢 Normal | -0.020 |  |
| 2026-04-15 08:00:40 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-04-15 08:00:33 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.045 |  |
| 2026-04-15 08:00:08 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-15 07:37:29 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.014 |  |
| 2026-04-15 07:21:42 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | -0.014 |  |
| 2026-04-15 07:16:16 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 07:00:17 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-15 08:03:42 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-15 08:01:04 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-15 07:09:47 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-15 08:00:08 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-15 08:02:20 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-15 08:02:25 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 08:02:44 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-15 08:03:15 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 08:04:55 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-15 08:02:41 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-15 08:03:38 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-15 08:01:55 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-15 08:02:52 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-04-15 08:02:07 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-15 07:10:07 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-15 08:06:37 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | -0.009 |  |
| 2026-04-15 07:06:25 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-04-15 08:01:54 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-04-15 08:01:50 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-04-15 08:00:40 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-04-15 08:02:14 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-04-15 08:04:24 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | -0.011 |  |
| 2026-04-15 08:05:18 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.012 |  |
| 2026-04-15 08:05:36 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | -0.014 |  |
| 2026-04-15 07:37:29 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.014 |  |
| 2026-04-15 08:00:47 | Thanthirimale (Malwathu Oya) | 2.78 | 🟢 Normal | -0.020 |  |
| 2026-04-15 08:00:49 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-04-15 08:02:30 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.022 |  |
| 2026-04-15 08:04:27 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | -0.039 |  |
| 2026-04-15 08:00:33 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.045 |  |
| 2026-04-15 08:03:21 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | -0.049 |  |
| 2026-04-15 08:02:59 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.050 |  |
| 2026-04-15 08:06:29 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.060 |  |
| 2026-04-14 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.063 |  |
| 2026-04-15 08:04:04 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.066 |  |
| 2026-04-15 08:04:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.088 |  |
| 2026-04-15 08:04:40 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.109 |  |
| 2026-04-15 08:01:08 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.139 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)