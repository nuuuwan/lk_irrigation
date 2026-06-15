# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--15_05:54:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **179,751 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-15 05:54:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.61 | 🟡 Alert | -0.424 |  |
| 2026-06-15 05:38:54 | Putupaula (Kalu Ganga) | 2.34 | 🟢 Normal | -0.027 |  |
| 2026-06-15 05:32:30 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.124 |  |
| 2026-06-15 05:30:35 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.015 |  |
| 2026-06-15 05:28:18 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -10.125 |  |
| 2026-06-15 05:27:46 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -10.125 |  |
| 2026-06-15 05:16:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.88 | 🟡 Alert | -0.424 |  |
| 2026-06-15 05:11:56 | Baddegama (Gin Ganga) | 2.27 | 🟢 Normal | -0.019 |  |
| 2026-06-15 05:11:43 | Rathnapura (Kalu Ganga) | 2.27 | 🟢 Normal | -0.034 |  |
| 2026-06-15 05:09:36 | Hanwella (Kelani Ganga) | 2.84 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-15 05:09:22 | Panadugama (Nilwala Ganga) | 3.38 | 🟢 Normal | -0.029 |  |
| 2026-06-15 05:08:51 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-15 05:07:00 | Dunamale (Aththanagalu Oya) | 2.45 | 🟢 Normal | -0.083 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-15 05:54:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.61 | 🟡 Alert | -0.424 |  |
| 2026-06-15 05:01:12 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 54.000 | 🔺 Rising |
| 2026-06-15 05:00:22 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-15 05:09:36 | Hanwella (Kelani Ganga) | 2.84 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-15 05:02:04 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-15 05:00:25 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-15 05:01:57 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-15 05:02:51 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-15 05:03:06 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-06-15 04:03:33 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-15 03:00:22 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-15 05:03:08 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-15 05:00:59 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-15 04:03:03 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-15 05:08:51 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-15 05:02:09 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-14 18:04:23 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.009 |  |
| 2026-06-15 05:04:48 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-06-14 18:01:41 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-06-15 05:03:39 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-06-15 05:05:09 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | -0.010 |  |
| 2026-06-15 05:01:04 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-06-15 05:02:48 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-06-15 05:30:35 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.015 |  |
| 2026-06-15 05:11:56 | Baddegama (Gin Ganga) | 2.27 | 🟢 Normal | -0.019 |  |
| 2026-06-14 18:03:42 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-06-15 05:06:16 | Magura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.022 |  |
| 2026-06-15 05:38:54 | Putupaula (Kalu Ganga) | 2.34 | 🟢 Normal | -0.027 |  |
| 2026-06-15 05:09:22 | Panadugama (Nilwala Ganga) | 3.38 | 🟢 Normal | -0.029 |  |
| 2026-06-15 05:01:15 | Moragaswewa (Deduru Oya) | 0.80 | 🟢 Normal | -0.033 |  |
| 2026-06-15 05:11:43 | Rathnapura (Kalu Ganga) | 2.27 | 🟢 Normal | -0.034 |  |
| 2026-06-15 05:05:18 | Glencourse (Kelani Ganga) | 10.76 | 🟢 Normal | -0.039 |  |
| 2026-06-15 05:02:04 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.040 |  |
| 2026-06-15 04:08:56 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.061 |  |
| 2026-06-15 05:01:32 | Ellagawa (Kalu Ganga) | 6.95 | 🟢 Normal | -0.070 |  |
| 2026-06-15 05:07:00 | Dunamale (Aththanagalu Oya) | 2.45 | 🟢 Normal | -0.083 |  |
| 2026-06-15 05:32:30 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.124 |  |
| 2026-06-15 05:01:26 | Peradeniya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.145 |  |
| 2026-06-15 05:28:18 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -10.125 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)