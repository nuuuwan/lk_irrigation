# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_18:49:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **135,772 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 18:49:37 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-04-26 18:16:35 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-26 18:13:56 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-04-26 18:10:01 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | 0.000 |  |
| 2026-04-26 18:07:41 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-26 18:07:26 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-04-26 18:06:57 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-26 18:06:09 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.009 |  |
| 2026-04-26 18:05:20 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 18:05:13 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-26 18:04:59 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-04-26 18:04:56 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | -0.010 |  |
| 2026-04-26 18:04:38 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-04-26 18:04:31 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-04-26 18:03:57 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-26 18:03:51 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.029 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 18:13:56 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-04-26 18:04:31 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-04-26 18:02:41 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-04-26 18:07:26 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-04-26 18:03:01 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-26 18:00:26 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-26 18:03:29 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-26 18:16:35 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-26 18:01:22 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-26 18:49:37 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-04-26 18:00:28 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-04-26 18:03:57 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-26 18:05:13 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-26 18:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-26 18:05:20 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 18:03:09 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-26 18:07:41 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-26 18:02:07 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-04-26 18:06:57 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-26 18:02:27 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-26 18:10:01 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | 0.000 |  |
| 2026-04-26 18:03:07 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-26 18:04:59 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-04-26 18:02:28 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-26 18:01:22 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-26 18:01:10 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-04-26 18:06:09 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.009 |  |
| 2026-04-26 18:01:48 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-04-26 18:01:48 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-04-26 18:04:56 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | -0.010 |  |
| 2026-04-26 18:04:38 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-04-26 18:02:26 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-04-26 18:03:35 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-04-26 18:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.020 |  |
| 2026-04-26 18:01:17 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.020 |  |
| 2026-04-26 18:03:20 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | -0.025 |  |
| 2026-04-26 18:03:51 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.029 |  |
| 2026-04-26 18:02:49 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.031 |  |
| 2026-04-26 18:00:25 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.039 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)