# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--28_07:01:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **109,412 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-28 07:01:03 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.052 |  |
| 2026-03-28 07:00:52 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.001 |  |
| 2026-03-28 06:33:15 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.003 |  |
| 2026-03-28 06:26:15 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.052 |  |
| 2026-03-28 06:24:46 | Horowpothana (Yan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-28 06:23:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-03-28 06:11:49 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-28 06:10:36 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-28 06:08:35 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-28 06:08:03 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-28 06:07:20 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-28 06:01:50 | Weraganthota (Mahaweli Ganga) | -2.14 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-03-28 06:23:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-03-28 06:04:55 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-03-28 06:02:17 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-28 06:03:04 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-28 06:33:15 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.003 |  |
| 2026-03-28 07:00:52 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.001 |  |
| 2026-03-28 06:02:58 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-28 06:01:26 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-28 06:10:36 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-28 06:01:08 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-28 06:03:37 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-28 06:24:46 | Horowpothana (Yan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-28 06:01:36 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-28 06:02:35 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-28 06:03:49 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-28 06:08:35 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-28 06:06:39 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-28 06:02:21 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-28 06:05:11 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-03-28 06:03:52 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-28 06:11:49 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-28 06:03:06 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-28 06:05:53 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-28 06:02:45 | Manampitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-28 06:02:40 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-28 06:06:48 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-28 06:07:20 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-28 06:08:03 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-28 06:04:54 | Badalgama (Maha Oya) | 1.69 | 🟢 Normal | -0.007 |  |
| 2026-03-28 06:04:35 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-03-28 06:00:09 | Ellagawa (Kalu Ganga) | 3.67 | 🟢 Normal | -0.010 |  |
| 2026-03-28 06:00:50 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-03-28 06:02:20 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.020 |  |
| 2026-03-28 06:02:34 | Hanwella (Kelani Ganga) | 0.16 | 🟢 Normal | -0.040 |  |
| 2026-03-28 06:04:35 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.040 |  |
| 2026-03-28 07:01:03 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.052 |  |
| 2026-03-28 06:01:29 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.084 |  |
| 2026-03-28 06:03:27 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)