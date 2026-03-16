# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--16_07:06:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **98,688 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 07:06:33 | Baddegama (Gin Ganga) | 0.34 | 🟢 Normal | -69.231 |  |
| 2026-03-16 07:06:17 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | -0.009 |  |
| 2026-03-16 07:06:12 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-16 07:06:07 | Baddegama (Gin Ganga) | 0.84 | 🟢 Normal | -69.231 |  |
| 2026-03-16 07:06:05 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | -0.012 |  |
| 2026-03-16 07:06:04 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-16 07:05:19 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | -0.009 |  |
| 2026-03-16 07:04:00 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.021 |  |
| 2026-03-16 07:03:31 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-16 07:03:14 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-03-16 07:03:05 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | -0.060 |  |
| 2026-03-16 07:02:50 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 07:02:41 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.258 |  |
| 2026-03-16 07:02:32 | Weraganthota (Mahaweli Ganga) | -2.47 | 🟢 Normal | -0.020 |  |
| 2026-03-16 07:02:29 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-16 07:02:23 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-03-16 07:02:15 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-03-16 07:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.63 | 🟢 Normal | -0.088 |  |
| 2026-03-16 07:02:01 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-03-16 07:01:42 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-03-16 07:01:37 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-16 07:01:34 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-16 07:01:28 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-16 07:01:24 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-03-16 07:00:52 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-03-16 07:00:52 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:35:06 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:16:13 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | -0.012 |  |
| 2026-03-16 06:13:37 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:12:59 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.258 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 07:03:14 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-03-16 07:02:01 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-03-16 07:02:23 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-03-16 06:04:43 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-16 07:02:50 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 06:05:04 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-16 07:02:29 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-16 07:01:28 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:01:43 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-16 07:01:42 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:13:37 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-16 07:06:12 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:02:37 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:03:40 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:01:56 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-16 07:03:31 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-16 07:01:34 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-16 07:01:37 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:02:50 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-16 07:00:52 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:02:20 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:04:02 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-16 07:06:04 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-16 07:02:15 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-03-16 07:06:17 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | -0.009 |  |
| 2026-03-16 07:05:19 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | -0.009 |  |
| 2026-03-16 06:09:51 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-16 07:01:24 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-03-16 07:06:05 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | -0.012 |  |
| 2026-03-16 07:02:32 | Weraganthota (Mahaweli Ganga) | -2.47 | 🟢 Normal | -0.020 |  |
| 2026-03-16 06:01:55 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-03-16 07:00:52 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-03-16 07:04:00 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.021 |  |
| 2026-03-16 06:02:39 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.041 |  |
| 2026-03-16 06:06:57 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.055 |  |
| 2026-03-16 07:03:05 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | -0.060 |  |
| 2026-03-16 07:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.63 | 🟢 Normal | -0.088 |  |
| 2026-03-16 07:02:41 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.258 |  |
| 2026-03-16 07:06:33 | Baddegama (Gin Ganga) | 0.34 | 🟢 Normal | -69.231 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)