# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--14_07:00:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **96,879 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 07:00:19 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-03-14 07:00:16 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 06:35:57 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-14 06:32:23 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-03-14 06:12:01 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.058 |  |
| 2026-03-14 06:11:41 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | -0.051 |  |
| 2026-03-14 06:06:56 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-14 06:06:53 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-14 06:06:50 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-14 06:06:01 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | -72.000 |  |
| 2026-03-14 06:06:00 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | -72.000 |  |
| 2026-03-14 06:05:49 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 06:32:23 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-03-14 06:05:27 | Moragaswewa (Deduru Oya) | 0.13 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-14 06:01:51 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-14 06:35:57 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-14 06:06:50 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-14 06:04:17 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.005 |  |
| 2026-03-14 07:00:16 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 06:03:25 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-14 06:03:48 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-03-14 05:44:26 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 06:06:53 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-14 06:06:56 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-14 06:03:16 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | 0.000 |  |
| 2026-03-14 06:03:18 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 06:01:33 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-14 06:02:30 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-14 06:03:51 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-14 06:05:49 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:02:59 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-14 06:02:44 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-14 06:04:13 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-14 07:00:19 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-03-14 06:04:22 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.014 |  |
| 2026-03-14 06:05:16 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.019 |  |
| 2026-03-14 06:01:23 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.021 |  |
| 2026-03-14 06:05:28 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.021 |  |
| 2026-03-14 06:00:49 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.021 |  |
| 2026-03-14 06:02:37 | Wellawaya (Kirindi Oya) | 0.77 | 🟢 Normal | -0.029 |  |
| 2026-03-14 06:04:02 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | -0.029 |  |
| 2026-03-14 06:05:31 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.039 |  |
| 2026-03-14 06:11:41 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | -0.051 |  |
| 2026-03-14 06:12:01 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.058 |  |
| 2026-03-14 06:04:25 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.080 |  |
| 2026-03-14 06:01:29 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.083 |  |
| 2026-03-14 06:00:54 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.099 |  |
| 2026-03-14 06:02:12 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.108 |  |
| 2026-03-14 06:01:14 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.173 |  |
| 2026-03-14 06:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.11 | 🟢 Normal | -0.443 |  |
| 2026-03-14 06:06:01 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)