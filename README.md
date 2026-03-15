# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--16_05:09:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **98,613 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 05:09:30 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-16 05:08:40 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-16 05:08:15 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-16 05:08:14 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-16 05:07:36 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-16 05:07:19 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-03-16 05:07:16 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-16 05:06:33 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.030 |  |
| 2026-03-16 05:06:26 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-16 05:06:15 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -36.000 |  |
| 2026-03-16 05:06:13 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -36.000 |  |
| 2026-03-16 05:04:14 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 05:04:06 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-03-16 05:03:44 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 05:03:42 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 05:03:42 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-16 05:03:34 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-16 05:03:34 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.045 |  |
| 2026-03-16 05:03:14 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | -0.080 |  |
| 2026-03-16 05:01:35 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 05:01:31 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | -0.073 |  |
| 2026-03-16 05:01:27 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-16 05:01:14 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-03-16 05:01:10 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.071 |  |
| 2026-03-16 05:00:56 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.021 |  |
| 2026-03-16 05:00:24 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:18:03 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:16:05 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.041 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 03:04:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 1.662 | 🔺 Rising |
| 2026-03-16 05:04:06 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-03-16 04:16:05 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-16 04:14:10 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-03-16 05:03:42 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-16 05:01:35 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 03:02:47 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 05:09:30 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-16 05:06:26 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:02:59 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:01:42 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:05:04 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-16 05:03:44 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 05:08:15 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:03:13 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:18:03 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-03-16 05:03:34 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-16 05:00:24 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-16 05:07:36 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:00:57 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 05:04:14 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 05:07:16 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:02:20 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-16 05:08:40 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-16 05:01:27 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:02:32 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-03-16 04:03:02 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.005 |  |
| 2026-03-16 05:07:19 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-03-16 05:01:14 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-03-16 05:00:56 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.021 |  |
| 2026-03-16 04:04:56 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.022 |  |
| 2026-03-16 05:06:33 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.030 |  |
| 2026-03-15 18:02:59 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.040 |  |
| 2026-03-16 05:03:34 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.045 |  |
| 2026-03-16 04:10:12 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.066 |  |
| 2026-03-16 05:01:10 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.071 |  |
| 2026-03-16 05:01:31 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | -0.073 |  |
| 2026-03-16 05:03:14 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | -0.080 |  |
| 2026-03-16 05:06:15 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)