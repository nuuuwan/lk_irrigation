# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--13_07:01:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **71,684 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 07:01:23 | Weraganthota (Mahaweli Ganga) | -2.07 | 🟢 Normal | -0.122 |  |
| 2026-02-13 07:01:11 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-13 07:00:12 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-02-13 06:30:05 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-13 06:24:08 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-13 06:13:39 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.019 |  |
| 2026-02-13 06:11:40 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 06:08:37 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-13 06:07:33 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-13 06:07:26 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-13 06:07:16 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.138 |  |
| 2026-02-13 06:06:55 | Padiyathalawa (Maduru Oya) | 0.99 | 🟢 Normal | -0.114 |  |
| 2026-02-13 06:06:19 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-13 06:06:19 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-13 06:06:11 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-13 06:05:41 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | -0.009 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 06:00:56 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.277 | 🔺 Rising |
| 2026-02-13 06:03:07 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-02-13 06:01:38 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-02-13 06:00:28 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-02-13 07:00:12 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-02-13 06:07:26 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-13 06:03:33 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-13 06:24:08 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-13 06:08:37 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-13 06:01:25 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-13 06:01:11 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-13 06:07:33 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-13 06:04:37 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 06:11:40 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 06:00:50 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-13 07:01:11 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-13 06:00:29 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-13 06:02:55 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-13 06:01:07 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-13 06:30:05 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-13 06:02:19 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-13 06:06:19 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-13 06:06:19 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-13 06:02:17 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-13 06:06:11 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-13 06:03:29 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-12 18:01:34 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-13 06:03:29 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-13 06:05:41 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | -0.009 |  |
| 2026-02-13 06:03:39 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-02-13 06:04:00 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.012 |  |
| 2026-02-13 06:04:05 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.012 |  |
| 2026-02-13 06:13:39 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.019 |  |
| 2026-02-13 06:03:19 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-02-13 06:06:55 | Padiyathalawa (Maduru Oya) | 0.99 | 🟢 Normal | -0.114 |  |
| 2026-02-13 07:01:23 | Weraganthota (Mahaweli Ganga) | -2.07 | 🟢 Normal | -0.122 |  |
| 2026-02-13 06:07:16 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.138 |  |
| 2026-02-13 06:04:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.66 | 🟢 Normal | -0.285 |  |
| 2026-02-13 06:05:05 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.384 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)