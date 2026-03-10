# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--10_07:00:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **94,099 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-10 07:00:41 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-03-10 07:00:25 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:00:18 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-10 06:44:41 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-03-10 06:40:33 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-10 06:22:55 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | -0.008 |  |
| 2026-03-10 06:19:33 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-03-10 06:14:50 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.072 |  |
| 2026-03-10 06:13:17 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-10 06:12:25 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.110 |  |
| 2026-03-10 06:11:50 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-03-10 06:10:54 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-10 06:10:45 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | -36.000 |  |
| 2026-03-10 06:10:44 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | -36.000 |  |
| 2026-03-10 06:10:43 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | -36.000 |  |
| 2026-03-10 06:10:42 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | -36.000 |  |
| 2026-03-10 06:10:41 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | -36.000 |  |
| 2026-03-10 06:10:40 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | -36.000 |  |
| 2026-03-10 06:10:38 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | -36.000 |  |
| 2026-03-10 06:10:37 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | -36.000 |  |
| 2026-03-10 06:10:35 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | -36.000 |  |
| 2026-03-10 06:09:14 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-10 06:07:50 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 06:07:00 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-10 06:06:48 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-03-10 06:06:42 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 06:06:00 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-03-10 06:05:56 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-10 06:01:36 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.392 | 🔺 Rising |
| 2026-03-10 07:00:41 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-03-09 18:01:06 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-03-10 06:19:33 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-03-10 06:01:02 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-10 06:06:48 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-03-10 06:07:00 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-10 06:01:54 | Weraganthota (Mahaweli Ganga) | -2.47 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-03-10 06:03:08 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 06:06:42 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 06:00:16 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:37:09 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-10 06:05:56 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-10 06:02:42 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-10 06:10:54 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:00:25 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-10 06:40:33 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-10 06:07:50 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 06:01:19 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-10 06:06:00 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-03-10 06:44:41 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:00:18 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-10 06:13:17 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-10 06:02:38 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-10 06:05:30 | Dunamale (Aththanagalu Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-10 06:05:10 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-10 06:04:36 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-10 06:09:14 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-10 06:03:52 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-10 05:59:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-10 06:22:55 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | -0.008 |  |
| 2026-03-10 06:11:50 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-03-10 06:02:12 | Thawalama (Gin Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-03-10 06:02:17 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.033 |  |
| 2026-03-10 06:03:54 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.038 |  |
| 2026-03-10 06:01:46 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.040 |  |
| 2026-03-10 06:14:50 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.072 |  |
| 2026-03-10 06:12:25 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.110 |  |
| 2026-03-10 06:10:45 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)