# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--18_07:03:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **182,469 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 07:03:50 | Hanwella (Kelani Ganga) | 2.75 | 🟢 Normal | -0.052 |  |
| 2026-06-18 07:03:49 | Panadugama (Nilwala Ganga) | 3.82 | 🟢 Normal | -0.011 |  |
| 2026-06-18 07:03:38 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-18 07:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.11 | 🟢 Normal | -0.090 |  |
| 2026-06-18 07:02:39 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-18 07:02:28 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.020 |  |
| 2026-06-18 07:02:26 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-18 07:02:16 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 07:02:16 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-18 07:02:15 | Ellagawa (Kalu Ganga) | 6.23 | 🟢 Normal | -0.042 |  |
| 2026-06-18 07:02:13 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.132 |  |
| 2026-06-18 07:02:11 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.020 |  |
| 2026-06-18 07:01:47 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.040 |  |
| 2026-06-18 07:01:44 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-18 07:01:43 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-06-18 07:01:34 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-18 07:00:50 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 07:00:42 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | -0.012 |  |
| 2026-06-18 07:00:19 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-06-18 07:00:14 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-18 06:30:46 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | -0.002 |  |
| 2026-06-18 06:23:24 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 07:00:19 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-06-18 07:03:38 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-18 07:02:26 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-18 06:01:01 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-18 07:00:50 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 07:02:16 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 06:04:10 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.005 |  |
| 2026-06-18 06:04:11 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-18 07:02:16 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-18 07:00:14 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-18 07:01:43 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-06-18 07:01:44 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-18 06:03:23 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-18 06:07:01 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 06:01:09 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-18 07:02:39 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-06-18 07:01:34 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-18 05:06:53 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-18 06:30:46 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | -0.002 |  |
| 2026-06-17 18:01:25 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-06-18 06:23:24 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-06-18 06:02:51 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | -0.010 |  |
| 2026-06-18 07:03:49 | Panadugama (Nilwala Ganga) | 3.82 | 🟢 Normal | -0.011 |  |
| 2026-06-18 07:00:42 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | -0.012 |  |
| 2026-06-18 07:02:11 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.020 |  |
| 2026-06-18 07:02:28 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.020 |  |
| 2026-06-18 06:01:24 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.022 |  |
| 2026-06-18 06:02:36 | Magura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.022 |  |
| 2026-06-18 06:05:45 | Peradeniya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.038 |  |
| 2026-06-18 07:01:47 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.040 |  |
| 2026-06-18 07:02:15 | Ellagawa (Kalu Ganga) | 6.23 | 🟢 Normal | -0.042 |  |
| 2026-06-18 07:03:50 | Hanwella (Kelani Ganga) | 2.75 | 🟢 Normal | -0.052 |  |
| 2026-06-18 07:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.11 | 🟢 Normal | -0.090 |  |
| 2026-06-18 06:01:06 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.091 |  |
| 2026-06-18 06:01:52 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.124 |  |
| 2026-06-18 07:02:13 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.132 |  |
| 2026-06-18 06:04:12 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | -0.134 |  |
| 2026-06-18 06:03:01 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.148 |  |
| 2026-06-18 06:03:53 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.210 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)