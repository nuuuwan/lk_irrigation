# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--03_06:01:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **169,037 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-03 06:01:53 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | -0.049 |  |
| 2026-06-03 06:01:52 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-03 06:01:50 | Rathnapura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.033 |  |
| 2026-06-03 06:01:32 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.061 |  |
| 2026-06-03 06:01:28 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-03 06:01:25 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-03 06:01:21 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-03 06:01:17 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-03 06:00:52 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 06:00:45 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-03 06:00:45 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-06-03 05:27:53 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.042 |  |
| 2026-06-03 05:21:48 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-06-03 05:14:04 | Magura (Kalu Ganga) | 1.77 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-03 05:12:42 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.061 |  |
| 2026-06-03 05:09:19 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-06-03 05:09:17 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-03 05:01:14 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.852 | 🔺 Rising |
| 2026-06-03 05:02:16 | Hanwella (Kelani Ganga) | 1.49 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-06-03 05:05:18 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-03 05:00:53 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-03 05:09:17 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-03 05:07:40 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-03 06:00:45 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-06-03 06:01:28 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-03 06:00:52 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 05:07:00 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-06-03 06:01:25 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-03 05:01:52 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-03 06:01:21 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-03 05:04:48 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-03 06:00:45 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-02 18:00:09 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-03 05:05:36 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-03 05:05:06 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-03 05:21:48 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-06-03 05:04:03 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-03 05:01:01 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-03 05:07:22 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-03 06:01:17 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-03 05:03:44 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-03 05:03:12 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-06-03 06:01:52 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-03 05:01:14 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-06-02 18:04:24 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-03 05:01:09 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-03 05:04:15 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-06-03 05:04:12 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | -0.012 |  |
| 2026-06-03 05:01:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.97 | 🟢 Normal | -0.012 |  |
| 2026-06-03 05:06:59 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.023 |  |
| 2026-06-03 05:09:19 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-06-03 06:01:50 | Rathnapura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.033 |  |
| 2026-06-03 05:27:53 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.042 |  |
| 2026-06-03 06:01:53 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | -0.049 |  |
| 2026-06-03 06:01:32 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.061 |  |
| 2026-06-03 05:01:06 | Peradeniya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)