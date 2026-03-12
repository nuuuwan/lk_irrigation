# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--12_07:18:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **95,135 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 07:18:52 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:18:24 | Thawalama (Gin Ganga) | 0.91 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-12 07:10:48 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.028 |  |
| 2026-03-12 07:10:33 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-03-12 07:08:49 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | -0.009 |  |
| 2026-03-12 07:08:26 | Hanwella (Kelani Ganga) | 0.91 | 🟢 Normal | 0.408 | 🔺 Rising |
| 2026-03-12 07:07:49 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-12 07:06:53 | Badalgama (Maha Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:06:23 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:06:11 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:05:11 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-12 07:05:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-03-12 07:05:00 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:04:49 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:04:38 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-03-12 07:04:28 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | -0.000 |  |
| 2026-03-12 07:03:34 | Manampitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:03:23 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:03:15 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-12 07:02:49 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:02:46 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.039 |  |
| 2026-03-12 07:02:43 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.043 |  |
| 2026-03-12 07:02:43 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-03-12 07:02:37 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:02:36 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-03-12 07:02:31 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:02:24 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:02:19 | Glencourse (Kelani Ganga) | 9.41 | 🟢 Normal | -0.143 |  |
| 2026-03-12 07:02:17 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:02:01 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:01:50 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:01:44 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | -0.139 |  |
| 2026-03-12 07:01:40 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:01:06 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:00:56 | Moraketiya (Walawe Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:00:34 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.137 |  |
| 2026-03-12 07:00:32 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 07:08:26 | Hanwella (Kelani Ganga) | 0.91 | 🟢 Normal | 0.408 | 🔺 Rising |
| 2026-03-12 07:07:49 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-12 07:10:33 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-03-12 07:03:15 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-12 07:18:24 | Thawalama (Gin Ganga) | 0.91 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-12 07:05:11 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-12 07:01:40 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:02:01 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:18:52 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:02:49 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:00:32 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:06:23 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:06:11 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:01:50 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:01:06 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:19:22 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:00:56 | Moraketiya (Walawe Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:02:37 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:05:00 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:02:17 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:02:31 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:06:53 | Badalgama (Maha Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:03:23 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:03:34 | Manampitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:05:34 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:04:49 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:02:24 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-12 07:04:28 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | -0.000 |  |
| 2026-03-12 07:08:49 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | -0.009 |  |
| 2026-03-12 07:02:43 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-03-12 07:05:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-03-12 07:04:38 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-03-12 07:02:36 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-03-12 07:10:48 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.028 |  |
| 2026-03-12 07:02:46 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.039 |  |
| 2026-03-12 07:02:43 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.043 |  |
| 2026-03-12 07:00:34 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.137 |  |
| 2026-03-12 07:01:44 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | -0.139 |  |
| 2026-03-12 07:02:19 | Glencourse (Kelani Ganga) | 9.41 | 🟢 Normal | -0.143 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)