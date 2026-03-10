# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--10_07:19:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **94,135 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-10 07:19:23 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:12:33 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:12:04 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:09:18 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-03-10 07:09:07 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-10 07:08:25 | Dunamale (Aththanagalu Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:07:50 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:07:18 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:06:30 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-10 07:06:25 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:05:59 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 07:05:59 | Thawalama (Gin Ganga) | 0.91 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-10 07:05:15 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:05:07 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-03-10 07:04:48 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.043 |  |
| 2026-03-10 07:04:45 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:04:31 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:04:21 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.176 |  |
| 2026-03-10 07:04:17 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.058 |  |
| 2026-03-10 07:03:28 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:03:17 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | 0.203 | 🔺 Rising |
| 2026-03-10 07:03:14 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | -0.012 |  |
| 2026-03-10 07:03:12 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:03:09 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-03-10 07:03:02 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.100 |  |
| 2026-03-10 07:02:57 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:02:45 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-03-10 07:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.076 |  |
| 2026-03-10 07:02:15 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.011 |  |
| 2026-03-10 07:02:09 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:01:56 | Weraganthota (Mahaweli Ganga) | -2.69 | 🟢 Normal | -0.220 |  |
| 2026-03-10 07:01:55 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.041 |  |
| 2026-03-10 07:01:44 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.031 |  |
| 2026-03-10 07:01:23 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:01:19 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:00:41 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-03-10 07:00:25 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:00:18 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-10 07:03:17 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | 0.203 | 🔺 Rising |
| 2026-03-10 07:00:41 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-03-10 07:09:07 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-10 07:05:59 | Thawalama (Gin Ganga) | 0.91 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-10 07:06:30 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-10 07:09:18 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-03-10 07:05:59 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 07:05:15 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:03:12 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:04:31 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:02:57 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:03:28 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:00:25 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:19:23 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:04:45 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:12:33 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:01:23 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:02:09 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:00:18 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:12:04 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:02:45 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:08:25 | Dunamale (Aththanagalu Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:07:18 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:06:25 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:07:50 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:01:19 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-10 07:05:07 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-03-10 07:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-03-10 07:03:09 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-03-10 07:02:15 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.011 |  |
| 2026-03-10 07:03:14 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | -0.012 |  |
| 2026-03-10 07:01:44 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.031 |  |
| 2026-03-10 07:01:55 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.041 |  |
| 2026-03-10 07:04:48 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.043 |  |
| 2026-03-10 07:04:17 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.058 |  |
| 2026-03-10 07:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.076 |  |
| 2026-03-10 07:03:02 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.100 |  |
| 2026-03-10 07:04:21 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.176 |  |
| 2026-03-10 07:01:56 | Weraganthota (Mahaweli Ganga) | -2.69 | 🟢 Normal | -0.220 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)