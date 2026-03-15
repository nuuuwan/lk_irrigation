# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--15_18:11:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **98,235 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 18:11:52 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-03-15 18:10:07 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:08:00 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-03-15 18:07:52 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:07:27 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.089 |  |
| 2026-03-15 18:07:09 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-15 18:06:31 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:06:13 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:06:00 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.060 |  |
| 2026-03-15 18:05:52 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-15 18:05:49 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:05:04 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:04:59 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:04:19 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.020 |  |
| 2026-03-15 18:04:16 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:03:57 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:03:49 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.012 |  |
| 2026-03-15 18:03:27 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:03:17 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:03:15 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:03:08 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:03:04 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | -0.020 |  |
| 2026-03-15 18:02:59 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.040 |  |
| 2026-03-15 18:02:57 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | -0.011 |  |
| 2026-03-15 18:02:54 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-03-15 18:02:48 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:02:28 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 18:02:20 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:02:14 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.030 |  |
| 2026-03-15 18:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.065 |  |
| 2026-03-15 18:02:07 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:01:19 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.044 |  |
| 2026-03-15 18:01:16 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 18:01:15 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:01:08 | Manampitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-15 18:01:01 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-03-15 18:00:43 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-15 18:00:33 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.063 |  |
| 2026-03-15 18:00:08 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 18:02:54 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-03-15 18:00:43 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-15 18:01:08 | Manampitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-15 18:07:09 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-15 18:02:28 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 18:01:16 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 18:05:52 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-15 18:02:48 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:03:08 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:01:15 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:10:07 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:05:04 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:05:49 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:03:27 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:06:31 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:03:57 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:04:59 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:03:17 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:00:08 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:03:15 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:07:52 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:04:16 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:02:20 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:06:13 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:08:00 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-03-15 18:11:52 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-03-15 18:01:01 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-03-15 17:00:37 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-03-15 18:02:57 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | -0.011 |  |
| 2026-03-15 18:03:49 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.012 |  |
| 2026-03-15 18:04:19 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.020 |  |
| 2026-03-15 18:03:04 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | -0.020 |  |
| 2026-03-15 18:02:14 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.030 |  |
| 2026-03-15 18:02:59 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.040 |  |
| 2026-03-15 18:01:19 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.044 |  |
| 2026-03-15 18:06:00 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.060 |  |
| 2026-03-15 18:00:33 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.063 |  |
| 2026-03-15 18:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.065 |  |
| 2026-03-15 18:07:27 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)