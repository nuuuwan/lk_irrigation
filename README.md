# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--20_17:13:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **211,523 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **3** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-20 17:13:52 | Thalgahagoda (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-20 17:10:13 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 17:08:24 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.009 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-20 17:00:39 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-07-20 17:05:03 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-20 17:03:45 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-07-20 17:02:17 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-20 17:02:13 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 17:03:07 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 17:06:05 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 17:04:13 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 17:08:24 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-20 17:03:21 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-20 17:00:35 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-20 17:03:35 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-20 17:01:23 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-20 17:04:17 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-20 17:01:04 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-20 17:01:32 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-20 17:06:42 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-20 17:01:53 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-20 17:03:44 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-20 17:03:24 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-20 17:05:28 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-20 17:04:32 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 17:03:52 | Glencourse (Kelani Ganga) | 9.12 | 🟢 Normal | 0.000 |  |
| 2026-07-20 17:04:53 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-20 17:01:47 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-07-20 17:07:33 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-20 17:02:16 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-20 17:04:11 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-20 17:10:13 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 17:13:52 | Thalgahagoda (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-20 17:01:32 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-20 17:02:11 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-07-20 17:03:23 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.012 |  |
| 2026-07-20 16:06:53 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-07-20 17:03:18 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.020 |  |
| 2026-07-20 17:07:03 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.028 |  |
| 2026-07-20 17:01:46 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.030 |  |
| 2026-07-20 17:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | -0.032 |  |
| 2026-07-20 17:05:30 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.041 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)