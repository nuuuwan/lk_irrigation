# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--19_07:00:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **77,033 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 07:00:35 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-19 07:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-19 07:00:09 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-19 06:50:57 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-19 06:32:23 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | -0.001 |  |
| 2026-02-19 06:13:57 | Padiyathalawa (Maduru Oya) | 1.12 | 🟢 Normal | -0.034 |  |
| 2026-02-19 06:10:12 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-19 06:08:47 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-19 06:07:51 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-02-19 06:06:48 | Dunamale (Aththanagalu Oya) | 0.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-19 06:06:38 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.126 |  |
| 2026-02-19 06:06:23 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-02-19 06:06:01 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 06:05:25 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.094 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 06:01:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-02-19 06:02:26 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-19 06:03:05 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-02-19 06:02:18 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-19 06:06:01 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 06:06:48 | Dunamale (Aththanagalu Oya) | 0.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-19 07:00:09 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-19 06:01:10 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-19 07:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-19 06:03:50 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-19 06:03:29 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 06:50:57 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-19 06:02:19 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-19 06:05:07 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-19 06:10:12 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-19 06:07:51 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-02-19 06:01:08 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-19 05:05:20 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-02-19 07:00:35 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-19 06:02:04 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-18 18:01:21 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-19 06:00:50 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-19 06:08:47 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-19 06:01:09 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-19 06:03:21 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-19 06:32:23 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | -0.001 |  |
| 2026-02-19 05:31:58 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.003 |  |
| 2026-02-19 06:06:23 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-02-19 06:04:23 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-02-19 06:03:22 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-02-19 06:03:07 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-02-19 06:04:28 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-02-19 06:01:55 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-02-19 06:13:57 | Padiyathalawa (Maduru Oya) | 1.12 | 🟢 Normal | -0.034 |  |
| 2026-02-19 06:01:52 | Weraganthota (Mahaweli Ganga) | -2.22 | 🟢 Normal | -0.036 |  |
| 2026-02-19 06:02:29 | Manampitiya (Mahaweli Ganga) | 2.45 | 🟢 Normal | -0.060 |  |
| 2026-02-19 06:05:25 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.094 |  |
| 2026-02-19 06:01:34 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.117 |  |
| 2026-02-19 06:06:38 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.126 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)