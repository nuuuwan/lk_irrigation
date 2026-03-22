# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--22_07:00:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **104,038 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-22 07:00:37 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-22 07:00:32 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-22 07:00:10 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-22 06:32:45 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-22 06:15:59 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | -0.025 |  |
| 2026-03-22 06:14:30 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-22 06:14:24 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-22 06:11:01 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.116 |  |
| 2026-03-22 06:07:14 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-22 06:06:52 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.019 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-22 06:02:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.37 | 🟢 Normal | 1.429 | 🔺 Rising |
| 2026-03-22 06:00:22 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-03-22 06:02:59 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-03-22 06:06:30 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-03-22 07:00:10 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-22 07:00:32 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-22 06:06:52 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-22 06:14:24 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-22 06:06:09 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-22 06:03:29 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-22 06:03:59 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-22 06:07:14 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-22 06:02:08 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-03-22 06:01:07 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-22 06:01:25 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-22 06:14:30 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-22 06:03:26 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-22 07:00:37 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-22 06:32:45 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-22 06:01:34 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-22 06:05:38 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-22 06:04:05 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-22 06:02:01 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-22 06:03:23 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-03-22 05:11:01 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-22 06:02:45 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-22 06:03:45 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-03-22 06:04:38 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-03-22 06:03:03 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | -0.010 |  |
| 2026-03-22 06:03:13 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-03-22 06:00:45 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-03-21 18:01:35 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-03-22 06:15:59 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | -0.025 |  |
| 2026-03-22 06:04:36 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.049 |  |
| 2026-03-22 06:02:52 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.089 |  |
| 2026-03-22 06:11:01 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.116 |  |
| 2026-03-22 06:04:21 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.138 |  |
| 2026-03-22 06:02:32 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.154 |  |
| 2026-03-22 06:01:39 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.193 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)